"""Report aggregate handler.

Seeded idiom: collections.OrderedDict where a plain dict now suffices (dicts
preserve insertion order since 3.7). Not removed; a soft 'improve, not
broken' modernization. Imports and passes on any interpreter.
"""
from collections import OrderedDict


def tally(events) -> dict:
    counts = OrderedDict()
    for event_name in events:
        counts[event_name] = counts.get(event_name, 0) + 1
    return dict(counts)


def lambda_handler(event, context):
    return {"statusCode": 200, "body": {"tally": tally(event.get("events", []))}}
