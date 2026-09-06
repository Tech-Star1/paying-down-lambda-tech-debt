from digest_handler import summarize, lambda_handler


def test_summarize_counts():
    assert summarize([1, 2, 3]) == "3 updates"
    assert summarize([]) == "0 updates"


def test_lambda_handler_summary():
    resp = lambda_handler({"items": ["a", "b"]}, None)
    assert resp["statusCode"] == 200
    assert resp["body"]["summary"] == "2 updates"
