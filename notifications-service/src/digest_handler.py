"""Digest handler.

Seeded idiom: locale.getdefaultlocale() (deprecated in 3.11; use
locale.setlocale / locale.getlocale). Valid on the 3.10 baseline. The
deprecated call is env-dependent so it is not asserted; the tested surface is
a pure summarizer.
"""
import locale


def resolve_locale(default: str = "en_US") -> str:
    # deprecated: getdefaultlocale() -> setlocale()/getlocale()
    try:
        code, _enc = locale.getdefaultlocale()
    except Exception:
        code = None
    return code or default


def summarize(items) -> str:
    return f"{len(items)} updates"


def lambda_handler(event, context):
    return {"statusCode": 200, "body": {"summary": summarize(event.get("items", []))}}
