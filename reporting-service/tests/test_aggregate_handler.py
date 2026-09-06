from aggregate_handler import tally, lambda_handler


def test_tally_counts():
    assert tally(["a", "b", "a", "c", "a"]) == {"a": 3, "b": 1, "c": 1}


def test_tally_empty():
    assert tally([]) == {}


def test_lambda_handler_tally():
    resp = lambda_handler({"events": ["x", "x", "y"]}, None)
    assert resp["statusCode"] == 200
    assert resp["body"]["tally"] == {"x": 2, "y": 1}
