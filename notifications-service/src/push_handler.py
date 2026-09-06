"""Push notification handler.

Seeded idiom: the `pipes` module (REMOVED in 3.13; use shlex.quote). Valid on
the 3.10 baseline. Removed call is in an untested path; the tested surface is
a pure priority mapping.
"""
import pipes  # removed in 3.13 -> shlex


def build_notify_command(token: str) -> str:
    return "notify-send " + pipes.quote(token)


def priority_for(kind: str) -> int:
    return {"alert": 1, "reminder": 2}.get(kind, 3)


def lambda_handler(event, context):
    return {"statusCode": 200, "body": {"priority": priority_for(event.get("kind", "info"))}}
