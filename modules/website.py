import requests
import socket
import time
from urllib.parse import urlparse
from datetime import datetime
from config import HEADERS

def normalize_url(target):
    if not target.startswith(("http://", "https://")):
        target = "https://" + target
    return target


def get_headers(response):
    wanted = [
        "Server",
        "Content-Type",
        "Content-Length",
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy",
        "Permissions-Policy"
    ]

    headers = {}

    for h in wanted:
        headers[h] = response.headers.get(h, "Not Present")

    return headers


def check_file(base_url, filename):
    try:
        r = requests.get(
            f"{base_url.rstrip('/')}/{filename}",
            headers=HEADERS,
            timeout=5
        )

        return {
            "exists": r.status_code == 200,
            "status_code": r.status_code
        }

    except Exception:
        return {
            "exists": False,
            "status_code": None
        }


def run(target):

    url = normalize_url(target)

    result = {
        "module": "Website Intelligence",
        "target": target,
        "success": False,
        "timestamp": str(datetime.now()),
        "data": {}
    }

    try:

        start = time.time()

        response = requests.get(
    url,
    headers=HEADERS,
    timeout=10,
    allow_redirects=True
        )

        elapsed = round((time.time() - start) * 1000, 2)

        host = urlparse(response.url).hostname

        ip = socket.gethostbyname(host)

        result["success"] = True

        result["data"] = {

            "url": response.url,

            "host": host,

            "ip_address": ip,

            "status_code": response.status_code,

            "response_time_ms": elapsed,

            "https": response.url.startswith("https://"),

            "redirected": response.history != [],

            "redirect_count": len(response.history),

            "server_headers": get_headers(response),

            "robots_txt": check_file(response.url, "robots.txt"),

            "sitemap_xml": check_file(response.url, "sitemap.xml")
        }

    except Exception as e:

        result["error"] = str(e)

    return result
