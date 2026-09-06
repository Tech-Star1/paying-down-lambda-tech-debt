"""Reconciliation handler.

Seeded idiom: datetime.utcnow().isoformat() (deprecated in 3.12).

THIS IS THE STRICT-PARITY GATE. The record timestamp is a naive UTC ISO
string with NO timezone suffix. The test asserts the exact naive format.
The obvious modernization, datetime.now(timezone.utc).isoformat(), appends
'+00:00' and CHANGES that string, so a naive transform breaks parity and the
validation gate routes it back. The behavior-preserving fix keeps the naive
format explicitly (e.g. datetime.now(timezone.utc).replace(tzinfo=None) or an
explicit strftime). Watch which one the agent produces.
"""
from datetime import datetime


def reconcile(txn_id: str, amount_cents: int, at: datetime) -> dict:
    """Build a reconciliation record. `at` is injected for deterministic tests."""
    return {
        "txn_id": txn_id,
        "amount_cents": amount_cents,
        # naive UTC, no offset suffix -- exact string is contractually asserted
        "reconciled_at": at.isoformat(),
    }


def lambda_handler(event, context):
    # production path uses utcnow(); tests inject `at` for determinism
    at = datetime.utcnow()
    record = reconcile(event["txn_id"], int(event["amount_cents"]), at)
    return {"statusCode": 200, "body": record}
