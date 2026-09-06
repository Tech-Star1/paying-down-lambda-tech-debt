from push_handler import priority_for, lambda_handler


def test_priority_known_kinds():
    assert priority_for("alert") == 1
    assert priority_for("reminder") == 2


def test_priority_default():
    assert priority_for("info") == 3
    assert priority_for("anything") == 3


def test_lambda_handler_priority():
    resp = lambda_handler({"kind": "alert"}, None)
    assert resp["statusCode"] == 200
    assert resp["body"]["priority"] == 1
