from export_handler import row_count, lambda_handler


def test_row_count():
    assert row_count([1, 2, 3]) == 3
    assert row_count([]) == 0


def test_lambda_handler_rows():
    resp = lambda_handler({"rows": ["a", "b"]}, None)
    assert resp["statusCode"] == 200
    assert resp["body"]["rows"] == 2
