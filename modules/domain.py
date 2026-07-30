import re
import whois
from .rdap import run as rdap

def validate_domain(domain):
    """
    Validate domain format.
    """
    pattern = r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.[A-Za-z]{2,}$"
    return re.match(pattern, domain) is not None


def format_value(value):
    """
    Format None, list and normal values.
    """
    if value is None:
        return "N/A"

    if isinstance(value, list):
        return ", ".join(str(v) for v in value)

    return str(value)


def run(target):

    print("\n" + "=" * 60)
    print("              DOMAIN INTELLIGENCE")
    print("=" * 60)

    if not validate_domain(target):
        print("\n[-] Invalid domain!")
        return

    try:

        data = whois.whois(target)
        if not data.registrar and not data.creation_date:
            data = rdap(target)
        print(f"\nTarget        : {target}")
        print(f"Registrar     : {format_value(data.registrar)}")
        print(f"Creation Date : {format_value(data.creation_date)}")
        print(f"Updated Date  : {format_value(data.updated_date)}")
        print(f"Expiry Date   : {format_value(data.expiration_date)}")
        print(f"Status        : {format_value(data.status)}")
        print(f"Name Servers  : {format_value(data.name_servers)}")
        
        return {
            "target": target,
            "registrar": format_value(data.registrar),
            "creation_date": format_value(data.creation_date),
            "updated_date": format_value(data.updated_date),
            "expiration_date": format_value(data.expiration_date),
            "status": format_value(data.status),
            "name_servers": format_value(data.name_servers),
        }
    except Exception as e:
        print(f"\n[-] WHOIS lookup failed")
        print(f"Reason : {e}")

    print("=" * 60)