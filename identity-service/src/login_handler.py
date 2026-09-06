"""Login handler.

Seeded idiom: asyncio.get_event_loop() with no running loop (deprecated
3.10+; asyncio.run() is the modern form). Valid on the 3.10 baseline.
"""
import asyncio


async def _check(username: str, password: str) -> bool:
    return bool(username) and len(password) >= 8


def verify_credentials(username: str, password: str) -> bool:
    # legacy: get_event_loop() with no running loop -> use asyncio.run()
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(_check(username, password))


def lambda_handler(event, context):
    ok = verify_credentials(event.get("username", ""), event.get("password", ""))
    return {"statusCode": 200 if ok else 401, "body": {"authenticated": ok}}
