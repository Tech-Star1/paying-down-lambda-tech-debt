from refund_handler import parse_full_refund, lambda_handler


def test_parse_full_refund_truthy_variants():
    assert parse_full_refund("yes") is True
    assert parse_full_refund("1") is True
    assert parse_full_refund("true") is True
    assert parse_full_refund(True) is True


def test_parse_full_refund_falsy_variants():
    assert parse_full_refund("no") is False
    assert parse_full_refund("0") is False
    assert parse_full_refund(False) is False


def test_lambda_handler_full_vs_partial():
    charge = {"net_cents": 9680}
    full = lambda_handler({"full_refund": "yes", "charge": charge}, None)
    partial = lambda_handler({"full_refund": "no", "charge": charge}, None)
    assert full["body"]["refund_cents"] == 9680
    assert partial["body"]["refund_cents"] == 4840
