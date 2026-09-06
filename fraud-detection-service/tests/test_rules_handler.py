from rules_handler import rulepack_current, lambda_handler


def test_rulepack_current_true():
    assert rulepack_current("2.0", "2.0") is True
    assert rulepack_current("2.1", "2.0") is True


def test_rulepack_current_false():
    assert rulepack_current("1.9", "2.0") is False


def test_lambda_handler_current():
    resp = lambda_handler({"installed": "3.0", "latest": "2.5"}, None)
    assert resp["statusCode"] == 200
    assert resp["body"]["current"] is True
