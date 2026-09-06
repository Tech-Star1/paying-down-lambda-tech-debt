from token_handler import scopes_for_role, lambda_handler


def test_scopes_admin():
    assert scopes_for_role("admin") == ["read", "write", "delete"]


def test_scopes_default_user():
    assert scopes_for_role("user") == ["read"]
    assert scopes_for_role("unknown") == []


def test_lambda_handler_returns_scopes():
    resp = lambda_handler({"role": "auditor"}, None)
    assert resp["statusCode"] == 200
    assert resp["body"]["scopes"] == ["read", "export"]
