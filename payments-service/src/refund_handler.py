"""Refund handler.

Seeded idiom: distutils.util.strtobool (distutils deprecated in 3.10 per
PEP 632, REMOVED in 3.12). Valid on the 3.10 baseline; must be modernized
(e.g. a local bool parser) to run on 3.13.
"""
from distutils.util import strtobool  # removed in 3.12


def parse_full_refund(flag) -> bool:
    """Coerce a truthy/falsy input ('yes'/'no'/'1'/'0'/'true') to bool."""
    if isinstance(flag, bool):
        return flag
    return bool(strtobool(str(flag)))


def lambda_handler(event, context):
    full = parse_full_refund(event.get("full_refund", "false"))
    net = int(event.get("charge", {}).get("net_cents", 0))
    refund_cents = net if full else net // 2
    return {"statusCode": 200, "body": {"full_refund": full, "refund_cents": refund_cents}}
