"""Settlement handler.

Seeded idiom: the `cgi` module (deprecated in 3.11 per PEP 594, REMOVED in
3.13). Valid on the 3.10 baseline; must be modernized (email.message /
urllib.parse) for 3.13. Used here to parse a settlement webhook's
Content-Type header.
"""
import cgi  # removed in 3.13


def content_kind(content_type_header: str) -> str:
    """Return the main content type from a header line, ignoring params."""
    main_value, _params = cgi.parse_header(content_type_header)
    return main_value


def lambda_handler(event, context):
    header = event.get("content_type", "application/json; charset=utf-8")
    kind = content_kind(header)
    settled = kind == "application/json"
    return {"statusCode": 200, "body": {"content_kind": kind, "settled": settled}}
