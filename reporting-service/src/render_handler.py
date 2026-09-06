"""Report render handler.

Seeded idiom: the `crypt` module (REMOVED in 3.13; use hashlib or a
maintained password library). Removed call is in an untested path; the
tested surface is a pure title formatter.
"""
import crypt  # removed in 3.13


def access_hash(token: str) -> str:
    return crypt.crypt(token, crypt.mksalt())


def title_for(report_type: str) -> str:
    return report_type.replace("_", " ").title()


def lambda_handler(event, context):
    return {"statusCode": 200, "body": {"title": title_for(event.get("report_type", "monthly_summary"))}}
