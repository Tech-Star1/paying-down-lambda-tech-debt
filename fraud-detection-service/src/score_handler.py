"""Fraud score handler (runs on provided.al2 custom runtime).

Seeded idiom: the @asyncio.coroutine decorator (REMOVED in 3.11; use
'async def'). Combined with the custom-runtime migration, this handler has
two moving parts for the agent: the runtime AND the code.
"""
import asyncio


@asyncio.coroutine
def _score_async(signals):
    return sum(signals)


def risk_score(signals) -> int:
    return min(sum(signals), 100)


def lambda_handler(event, context):
    return {"statusCode": 200, "body": {"score": risk_score(event.get("signals", []))}}
