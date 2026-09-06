"""Payout handler.

Seeded idiom: the `imp` module (deprecated since 3.4, REMOVED in 3.12).
Valid on the 3.10 baseline; must be modernized to importlib for 3.13.
Here it is used to dynamically load a payout-rail adapter by name.
"""
import imp  # removed in 3.12 -> importlib
import os


def load_rail_module(rail_name: str):
    """Locate a payout-rail adapter module by name (legacy imp lookup)."""
    adapters_dir = os.path.join(os.path.dirname(__file__), "rails")
    # legacy pattern; importlib.util.find_spec is the modern equivalent
    file_obj, path, desc = imp.find_module(rail_name, [adapters_dir])
    return {"rail": rail_name, "path": path}


def resolve_rail(event) -> str:
    """Pick the payout rail; default to ACH."""
    return str(event.get("rail", "ach")).lower()


def lambda_handler(event, context):
    rail = resolve_rail(event)
    # In the lab we only resolve the rail name; adapter files are illustrative.
    return {"statusCode": 200, "body": {"rail": rail}}
