"""Ledger posting handler (PCI-scoped domain).

Seeded idiom: datetime.utcfromtimestamp() (deprecated in 3.12).

PARITY GATE #2. The posting timestamp is a NAIVE UTC ISO string with no
offset (the audit-trail contract). The naive modernization
datetime.fromtimestamp(epoch, tz=timezone.utc) appends '+00:00' and changes
the string, failing validation and routing back. The behavior-preserving fix
keeps the naive format explicitly. In a PCI audit trail a silent timestamp
format change is exactly the kind of drift the validation gate must catch.
"""
from datetime import datetime


def post_entry(entry_id: str, amount_cents: int, epoch: int) -> dict:
    return {
        "entry_id": entry_id,
        "amount_cents": amount_cents,
        "posted_at": datetime.utcfromtimestamp(epoch).isoformat(),  # naive, no offset
    }


def lambda_handler(event, context):
    rec = post_entry(event["entry_id"], int(event["amount_cents"]), int(event.get("epoch", 0)))
    return {"statusCode": 200, "body": rec}
