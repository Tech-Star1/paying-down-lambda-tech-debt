"""Token handler.

Seeded idiom: typing.List / typing.Dict for annotations. Not removed, but a
soft modernization to builtin generics (list[str], dict[...]) available since
3.9. Shows the agent handling 'improve but not broken' cases.
"""
from typing import Dict, List


def scopes_for_role(role: str) -> List[str]:
    mapping: Dict[str, List[str]] = {
        "admin": ["read", "write", "delete"],
        "auditor": ["read", "export"],
        "user": ["read"],
    }
    return mapping.get(role, [])


def lambda_handler(event, context):
    scopes = scopes_for_role(event.get("role", "user"))
    return {"statusCode": 200, "body": {"scopes": scopes}}
