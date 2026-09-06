from payout_handler import resolve_rail, lambda_handler


def test_resolve_rail_default_is_ach():
    assert resolve_rail({}) == "ach"


def test_resolve_rail_lowercases():
    assert resolve_rail({"rail": "WIRE"}) == "wire"


def test_lambda_handler_returns_rail():
    resp = lambda_handler({"rail": "rtp"}, None)
    assert resp["statusCode"] == 200
    assert resp["body"] == {"rail": "rtp"}
