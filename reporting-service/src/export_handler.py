"""Report export handler.

Seeded idiom: the @asyncio.coroutine decorator (REMOVED in 3.11; use
'async def'). Applied at module load, so this module only imports on the
3.10 baseline. Tested surface is a pure row counter.
"""
import asyncio


@asyncio.coroutine
def _stream_rows(rows):
    for row in rows:
        yield row


def row_count(rows) -> int:
    return len(rows)


def lambda_handler(event, context):
    return {"statusCode": 200, "body": {"rows": row_count(event.get("rows", []))}}
