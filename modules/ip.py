
import ipaddress
import socket
import requests
from ipwhois import IPWhois
from datetime import datetime


def validate_ip(ip):
    try:
        return ipaddress.ip_address(ip)
    except ValueError:
        return None


def reverse_dns(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except Exception:
        return None


def get_geolocation(ip):
    try:
        response = requests.get(
            f"http://ip-api.com/json/{ip}",
            timeout=10
        )

        data = response.json()

        if data.get("status") == "success":
            return data

    except Exception:
        pass

    return {}


def get_rdap(ip):
    try:
        obj = IPWhois(ip)
        return obj.lookup_rdap(depth=1)
    except Exception:
        return {}


def run(target):

    ip = validate_ip(target)

    if ip is None:

        return {
            "module": "IP Intelligence",
            "target": target,
            "success": False,
            "timestamp": str(datetime.now()),
            "error": "Invalid IP Address",
            "data": {}
        }

    result = {
        "module": "IP Intelligence",
        "target": str(ip),
        "success": True,
        "timestamp": str(datetime.now()),
        "data": {}
    }

    result["data"]["version"] = ip.version
    result["data"]["private"] = ip.is_private
    result["data"]["loopback"] = ip.is_loopback
    result["data"]["multicast"] = ip.is_multicast
    result["data"]["reserved"] = ip.is_reserved

    rdap = get_rdap(str(ip))

    if rdap:

        network = rdap.get("network", {})

        result["data"]["rdap"] = {
            "asn": rdap.get("asn"),
            "asn_cidr": rdap.get("asn_cidr"),
            "asn_country": rdap.get("asn_country_code"),
            "asn_registry": rdap.get("asn_registry"),
            "network_name": network.get("name"),
            "network_country": network.get("country")
        }

    geo = get_geolocation(str(ip))

    if geo:

        result["data"]["geolocation"] = {
            "continent": geo.get("continent"),
            "country": geo.get("country"),
            "country_code": geo.get("countryCode"),
            "region": geo.get("regionName"),
            "city": geo.get("city"),
            "zip": geo.get("zip"),
            "latitude": geo.get("lat"),
            "longitude": geo.get("lon"),
            "timezone": geo.get("timezone"),
            "isp": geo.get("isp"),
            "organization": geo.get("org"),
            "as": geo.get("as")
        }

        result["data"]["google_maps"] = (
            f"https://maps.google.com/?q={geo.get('lat')},{geo.get('lon')}"
        )

    result["data"]["reverse_dns"] = reverse_dns(str(ip))

    return result