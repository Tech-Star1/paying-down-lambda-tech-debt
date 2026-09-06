"""SMS notification handler.

Seeded idiom: datetime.utcfromtimestamp() (deprecated in 3.12; use
datetime.fromtimestamp(epoch, tz=timezone.utc)). Valid on the 3.10 baseline
and still present through 3.14, so its test is deterministic on any modern
interpreter.
"""
from datetime import datetime


def format_sent_at(epoch: int) -> str:
    # deprecated: utcfromtimestamp -> fromtimestamp(epoch, tz=timezone.utc)
    return datetime.utcfromtimestamp(epoch).isoformat()


def truncate(body: str, limit: int = 160) -> str:
    return body[:limit]


def lambda_handler(event, context):
    text = truncate(event.get("body", ""))
    return {"statusCode": 200, "body": {"text": text, "sent_at": format_sent_at(int(event.get("epoch", 0)))}}
