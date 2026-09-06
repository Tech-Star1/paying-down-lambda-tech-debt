"""MFA handler.

Seeded idiom: ssl.wrap_socket() (REMOVED in 3.12; use
ssl.SSLContext.wrap_socket). The removed call sits in an untested network
path so the module still imports on any interpreter, but the version-upgrade
agent must still find and fix it. The tested surface is a pure challenge
generator.
"""
import socket
import ssl


def generate_challenge(secret: str) -> str:
    """Deterministic MFA challenge from a shared secret (tested surface)."""
    digest = sum(ord(c) for c in secret) % 1_000_000
    return "mfa-" + str(digest).zfill(6)


def open_secure_socket(host: str, port: int = 443):
    raw = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # legacy: ssl.wrap_socket removed in 3.12 -> SSLContext.wrap_socket
    return ssl.wrap_socket(raw)


def lambda_handler(event, context):
    return {"statusCode": 200, "body": {"challenge": generate_challenge(event.get("secret", ""))}}
