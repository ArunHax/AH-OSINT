import dns.resolver

resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = [
    "1.1.1.1",  # Cloudflare
    "8.8.8.8"   # Google
]

def lookup(target, record_type):
    """
    Returns a list of DNS records.
    """

    try:
        answers = resolver.resolve(target, record_type)
        return [str(answer) for answer in answers]

    except dns.resolver.NoAnswer:
        return []

    except dns.resolver.NXDOMAIN:
        return None

    except Exception:
        return []


def run(target):

    print("\n" + "=" * 60)
    print("                 DNS INTELLIGENCE")
    print("=" * 60)

    record_types = [
        "A",
        "AAAA",
        "MX",
        "NS",
        "TXT",
        "CNAME",
        "SOA"
    ]

    results = {}

    for record in record_types:
        data = lookup(target, record)

        if data is None:
            print("\n[-] Domain does not exist.")
            print("=" * 60)
            return

        results[record] = data

    # Print Results
    for record, values in results.items():

        print(f"\n{record} Records")
        print("-" * 60)

        if values:
            for value in values:
                print(value)
        else:
            print("No records found.")

    print("\n" + "=" * 60)

    return results
