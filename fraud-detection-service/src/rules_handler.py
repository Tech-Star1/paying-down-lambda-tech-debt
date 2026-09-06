"""Fraud rules handler (runs on provided.al2 custom runtime).

Seeded idiom: distutils.version.LooseVersion (REMOVED in 3.12; use
packaging.version.Version) for rule-pack version comparison.
"""
from distutils.version import LooseVersion  # removed in 3.12


def rulepack_current(installed: str, latest: str) -> bool:
    return LooseVersion(installed) >= LooseVersion(latest)


def lambda_handler(event, context):
    current = rulepack_current(event.get("installed", "1.0"), event.get("latest", "1.0"))
    return {"statusCode": 200, "body": {"current": current}}
