"""Ledger statement handler (PCI-scoped domain).

Seeded idiom: typing.List / typing.Optional annotations (soft modernization
to builtin generics and the X | None union available since 3.10). Not broken,
just datable. Imports and passes on any interpreter.
"""
from typing import List, Optional


def format_lines(lines: List[str], header: Optional[str] = None) -> List[str]:
    out = [header] if header else []
    out.extend(lines)
    return out


def lambda_handler(event, context):
    lines = format_lines(event.get("lines", []), event.get("header"))
    return {"statusCode": 200, "body": {"lines": lines}}
