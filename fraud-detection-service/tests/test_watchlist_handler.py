from watchlist_handler import matches, lambda_handler


def test_matches_case_insensitive():
    assert matches("John Doe", ["jane roe", "john doe"]) is True


def test_no_match():
    assert matches("Alice", ["bob", "carol"]) is False
    assert matches("", []) is False


def test_lambda_handler_match():
    resp = lambda_handler({"name": " Bob ", "watchlist": ["bob"]}, None)
    assert resp["statusCode"] == 200
    assert resp["body"]["match"] is True
