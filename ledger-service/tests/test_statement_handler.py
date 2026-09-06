from statement_handler import format_lines, lambda_handler


def test_format_lines_with_header():
    assert format_lines(["a", "b"], "STATEMENT") == ["STATEMENT", "a", "b"]


def test_format_lines_no_header():
    assert format_lines(["a", "b"]) == ["a", "b"]


def test_lambda_handler_lines():
    resp = lambda_handler({"lines": ["x"], "header": "H"}, None)
    assert resp["statusCode"] == 200
    assert resp["body"]["lines"] == ["H", "x"]
