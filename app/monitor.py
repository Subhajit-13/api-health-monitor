
import time
import requests
from urllib.parse import urlparse
import ipaddress


REQUEST_TIMEOUT_SECONDS = 5


def validate_url(url):
    if not url:
        return False, "Please enter a URL."

    try:
        parsed_url = urlparse(url)
    except ValueError:
        return False, "Please enter a valid URL."

    if parsed_url.scheme not in ("http", "https"):
        return False, "Only HTTP and HTTPS URLs are allowed."

    if not parsed_url.hostname:
        return False, "The URL must contain a hostname."

    if parsed_url.username or parsed_url.password:
        return False, "URLs containing credentials are not allowed."

    hostname = parsed_url.hostname.lower()

    if hostname == "localhost" or hostname.endswith(".localhost"):
        return False, "Localhost URLs are not allowed."

    try:
        ip_address = ipaddress.ip_address(hostname)
    except ValueError:
        ip_address = None

    if ip_address and not ip_address.is_global:
        return False, "Private or non-public IP addresses are not allowed."

    return True, None


def check_api(url):
    start_time = time.perf_counter()

    try:
        response = requests.get(
            url,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )

        reachable = True
        healthy = 200 <= response.status_code < 400

        return {
            "url": url,
            "reachable": reachable,
            "healthy": healthy,
            "status_code": response.status_code,
            "response_time_ms": round(
                (time.perf_counter() - start_time) * 1000, 2
            ),
            "error": None,
        }

    except requests.exceptions.RequestException as error:
        return {
            "url": url,
            "reachable": False,
            "healthy": False,
            "status_code": None,
            "response_time_ms": round(
                (time.perf_counter() - start_time) * 1000, 2
            ),
            "error": str(error),
        }
