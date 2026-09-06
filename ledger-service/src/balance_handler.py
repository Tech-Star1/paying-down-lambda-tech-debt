"""Ledger balance handler (PCI-scoped domain).

Seeded idiom: distutils.util.strtobool (REMOVED in 3.12). This idiom also
appears in payments-service on purpose: the SAME debt recurs across accounts,
and the batching model handles it consistently everywhere. Fix: a local bool
parser.
"""
from distutils.util import strtobool  # removed in 3.12


def is_reconciled(flag) -> bool:
    if isinstance(flag, bool):
        return flag
    return bool(strtobool(str(flag)))


def net_balance(credits_cents, debits_cents) -> int:
    return sum(credits_cents) - sum(debits_cents)


def lambda_handler(event, context):
    net = net_balance(event.get("credits", []), event.get("debits", []))
    reconciled = is_reconciled(event.get("reconciled", "false"))
    return {"statusCode": 200, "body": {"net_cents": net, "reconciled": reconciled}}
