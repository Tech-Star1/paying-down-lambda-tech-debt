"""Ledger audit handler (PCI-scoped domain).

Seeded idiom: invalid escape sequence in a plain-string regex (SyntaxWarning
in 3.12). Recurs from identity-service on purpose: lint-level debt is
everywhere. Fix: a raw string r"...".
"""
import re

# should be r"^GL-\d{6}$" -- "\d" is an invalid escape in a plain string
REF_RE = re.compile("^GL-\d{6}$")


def is_valid_ref(ref: str) -> bool:
    return bool(REF_RE.match(ref or ""))


def lambda_handler(event, context):
    valid = is_valid_ref(event.get("ref", ""))
    return {"statusCode": 200 if valid else 400, "body": {"valid": valid}}
