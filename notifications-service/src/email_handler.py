"""Email notification handler.

Seeded idiom: the `imghdr` module (REMOVED in 3.13) for attachment type
detection. Valid on the 3.10 baseline; fix is a content-type check or a
maintained file-type library. The removed call is in an untested path; the
tested surface is a pure extension allow-list.
"""
import imghdr  # removed in 3.13


def attachment_kind(data: bytes) -> str:
    return imghdr.what(None, h=data) or "unknown"


def is_allowed(filename: str) -> bool:
    return filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))


def lambda_handler(event, context):
    allowed = is_allowed(event.get("filename", ""))
    return {"statusCode": 200 if allowed else 415, "body": {"allowed": allowed}}
