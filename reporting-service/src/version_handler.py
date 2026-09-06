"""Report version handler.

Seeded idiom: distutils.version.LooseVersion (REMOVED in 3.12; use
packaging.version.Version). Valid on the 3.10 baseline.
"""
from distutils.version import LooseVersion  # removed in 3.12


def is_upgrade(current: str, candidate: str) -> bool:
    return LooseVersion(candidate) > LooseVersion(current)


def lambda_handler(event, context):
    up = is_upgrade(event.get("current", "1.0"), event.get("candidate", "1.0"))
    return {"statusCode": 200, "body": {"is_upgrade": up}}
