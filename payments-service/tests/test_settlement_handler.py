from settlement_handler import content_kind, lambda_handler


def test_content_kind_strips_params():
    assert content_kind("application/json; charset=utf-8") == "application/json"


def test_content_kind_plain():
    assert content_kind("text/csv") == "text/csv"


def test_lambda_handler_settled_on_json():
    resp = lambda_handler({"content_type": "application/json; charset=utf-8"}, None)
    assert resp["statusCode"] == 200
    assert resp["body"]["settled"] is True


def test_lambda_handler_not_settled_on_csv():
    resp = lambda_handler({"content_type": "text/csv"}, None)
    assert resp["body"]["settled"] is False
