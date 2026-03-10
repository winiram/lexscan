import ipaddress
import socket
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "LexScan-bot/1.0 (legal document summarizer; not for scraping)"
}
TIMEOUT = 15
JS_THRESHOLD = 200
MAX_RESPONSE_BYTES = 5 * 1024 * 1024  # 5 MB

_ALLOWED_SCHEMES = {"http", "https"}


def _validate_url(url: str) -> None:
    """Raise ValueError if the URL is unsafe (non-http/s scheme or private IP)."""
    parsed = urlparse(url)

    if parsed.scheme not in _ALLOWED_SCHEMES:
        raise ValueError(
            f"Only http:// and https:// URLs are supported (got '{parsed.scheme}://')."
        )

    hostname = parsed.hostname
    if not hostname:
        raise ValueError("URL has no hostname.")

    try:
        # Resolve all A/AAAA records and check each
        infos = socket.getaddrinfo(hostname, None)
    except socket.gaierror as exc:
        raise ValueError(f"Could not resolve hostname '{hostname}': {exc}") from exc

    for info in infos:
        addr_str = info[4][0]
        try:
            ip = ipaddress.ip_address(addr_str)
        except ValueError:
            continue
        if (
            ip.is_private
            or ip.is_loopback
            or ip.is_link_local
            or ip.is_reserved
            or ip.is_multicast
        ):
            raise ValueError(
                "Requests to private or internal network addresses are not allowed."
            )


def fetch_clean_text(url: str) -> str:
    """Fetch a URL and return its cleaned plain text.

    Raises ValueError with a human-readable message on failure.
    """
    # Validate before sending any request
    _validate_url(url)

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=TIMEOUT,
            stream=True,
            allow_redirects=True,
        )
        response.raise_for_status()
    except requests.exceptions.Timeout:
        raise ValueError(
            f"Request timed out after {TIMEOUT}s. The site may be slow or blocking scrapers."
        )
    except requests.exceptions.HTTPError as e:
        status = e.response.status_code if e.response is not None else "unknown"
        raise ValueError(
            f"HTTP {status} error fetching URL. The site may block automated access."
        )
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Network error: {e}")

    # Validate after any redirects (SSRF via redirect)
    _validate_url(response.url)

    # Cap response size to prevent memory exhaustion
    chunks = []
    total = 0
    for chunk in response.iter_content(chunk_size=65536, decode_unicode=False):
        total += len(chunk)
        if total > MAX_RESPONSE_BYTES:
            raise ValueError(
                "The page is too large to process (limit: 5 MB). "
                "Try copying the relevant section and using the Paste tab instead."
            )
        chunks.append(chunk)

    raw_bytes = b"".join(chunks)
    encoding = response.encoding or "utf-8"
    try:
        html_text = raw_bytes.decode(encoding, errors="replace")
    except LookupError:
        html_text = raw_bytes.decode("utf-8", errors="replace")

    soup = BeautifulSoup(html_text, "lxml")

    # Remove non-content tags
    for tag in soup(["script", "style", "nav", "footer", "header", "aside", "form"]):
        tag.decompose()

    text = soup.get_text(separator="\n", strip=True)

    # Collapse excessive blank lines
    lines = [line.strip() for line in text.splitlines()]
    cleaned_lines = []
    prev_blank = False
    for line in lines:
        if not line:
            if not prev_blank:
                cleaned_lines.append("")
            prev_blank = True
        else:
            cleaned_lines.append(line)
            prev_blank = False

    result = "\n".join(cleaned_lines).strip()

    if len(result) < JS_THRESHOLD:
        raise ValueError(
            "Very little text was found on this page — it may require JavaScript to render. "
            "Try copying the text manually and using the Paste tab instead."
        )

    return result
