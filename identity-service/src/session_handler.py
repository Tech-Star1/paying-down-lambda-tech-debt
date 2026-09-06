"""Session handler.

Seeded idiom: invalid escape sequences in a normal string literal ("\\d",
"\\{") which became a SyntaxWarning in 3.12 (DeprecationWarning earlier).
The fix is a raw string r"...". Valid and functional on the 3.10 baseline.
"""
import re

# should be r"^sess_\d{8}$" -- "\d" is an invalid escape in a plain string
TOKEN_RE = re.compile("^sess_\d{8}$")


def is_valid_session(token: str) -> bool:
    return bool(TOKEN_RE.match(token or ""))


def lambda_handler(event, context):
    valid = is_valid_session(event.get("session_token", ""))
    return {"statusCode": 200 if valid else 400, "body": {"valid": valid}}
