from score_handler import risk_score, lambda_handler


def test_risk_score_sums():
    assert risk_score([10, 20, 30]) == 60


def test_risk_score_caps_at_100():
    assert risk_score([60, 60]) == 100


def test_lambda_handler_score():
    resp = lambda_handler({"signals": [25, 25]}, None)
    assert resp["statusCode"] == 200
    assert resp["body"]["score"] == 50
