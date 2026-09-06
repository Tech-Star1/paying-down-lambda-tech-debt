"""Fraud watchlist handler (runs on provided.al2 custom runtime).

Seeded idiom: typing.List annotation (soft modernization to builtin generics,
3.9+). Imports and passes on any interpreter; the custom-runtime migration is
the primary transform here.
"""
from typing import List


def matches(name: str, watchlist: List[str]) -> bool:
    normalized = {w.strip().lower() for w in watchlist}
    return name.strip().lower() in normalized


def lambda_handler(event, context):
    hit = matches(event.get("name", ""), event.get("watchlist", []))
    return {"statusCode": 200, "body": {"match": hit}}
