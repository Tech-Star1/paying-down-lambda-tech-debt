from version_handler import is_upgrade, lambda_handler


def test_is_upgrade_true():
    assert is_upgrade("1.0", "2.0") is True
    assert is_upgrade("1.2.0", "1.10.0") is True


def test_is_upgrade_false():
    assert is_upgrade("2.0", "1.0") is False
    assert is_upgrade("1.0", "1.0") is False


def test_lambda_handler_is_upgrade():
    resp = lambda_handler({"current": "1.0", "candidate": "1.5"}, None)
    assert resp["statusCode"] == 200
    assert resp["body"]["is_upgrade"] is True
