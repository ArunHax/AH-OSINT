import re
import requests
from types import SimpleNamespace

def validate_domain(domain):
    pattern = r"^(?=.{1,253}$)(?!-)(?:[A-Za-z0-9-]{1,63}\.)+[A-Za-z]{2,63}$"
    return re.match(pattern, domain) is not None


def get_registrar(data):
    for entity in data.get("entities", []):
        if "registrar" in entity.get("roles", []):
            vcard = entity.get("vcardArray", [])
            if len(vcard) > 1:
                for item in vcard[1]:
                    if item[0] == "fn":
                        return item[3]
    return "N/A"


def get_event(events, action):
    for event in events:
        if event.get("eventAction", "").lower() == action.lower():
            return event.get("eventDate", "N/A")
    return "N/A"


def run(domain):
    if not validate_domain(domain):
        print("\n[-] Invalid domain!")
        return

    try:
        url = f"https://rdap.org/domain/{domain}"

        response = requests.get(
            url,
            headers={"Accept": "application/rdap+json"},
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        registrar = get_registrar(data)

        creation = get_event(data.get("events", []), "registration")
        updated = get_event(data.get("events", []), "last changed")
        expiry = get_event(data.get("events", []), "expiration")

        status = ", ".join(data.get("status", [])) or "N/A"

        nameservers = [
            ns.get("ldhName", "")
            for ns in data.get("nameservers", [])
        ]

        return SimpleNamespace(
            registrar=registrar,
            creation_date=creation,
            updated_date=updated,
            expiration_date=expiry,
            status=status,
            name_servers=nameservers,
        )

    except requests.HTTPError as e:
        print(f"\n[-] RDAP lookup failed (HTTP {e.response.status_code})")

    except Exception as e:
        print(f"\n[-] RDAP lookup failed")
        print(f"Reason : {e}")

    print("=" * 60)
