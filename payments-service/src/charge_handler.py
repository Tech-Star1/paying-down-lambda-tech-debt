"""Charge processing handler.

Seeded idiom: datetime.utcnow() (deprecated in Python 3.12).
This is a behavior-safe modernization case: the tested surface is the
fee math, so the timestamp modernization does not change assertions.
"""
from datetime import datetime


FEE_RATE = 0.029
FLAT_FEE_CENTS = 30


def calculate_charge(amount_cents: int) -> dict:
    """Return gross, fee, and net for a card charge, in cents."""
    fee = round(amount_cents * FEE_RATE) + FLAT_FEE_CENTS
    return {
        "gross_cents": amount_cents,
        "fee_cents": fee,
        "net_cents": amount_cents - fee,
    }


def lambda_handler(event, context):
    amount = int(event["amount_cents"])
    result = calculate_charge(amount)
    # deprecated: datetime.utcnow() -> use datetime.now(timezone.utc)
    result["processed_at"] = datetime.utcnow().isoformat()
    return {"statusCode": 200, "body": result}
