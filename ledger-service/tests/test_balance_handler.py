from balance_handler import net_balance, is_reconciled, lambda_handler


def test_net_balance():
    assert net_balance([1000, 500], [300]) == 1200
    assert net_balance([], []) == 0


def test_is_reconciled_variants():
    assert is_reconciled("yes") is True
    assert is_reconciled("0") is False
    assert is_reconciled(True) is True


def test_lambda_handler_balance():
    resp = lambda_handler({"credits": [1000], "debits": [400], "reconciled": "true"}, None)
    assert resp["statusCode"] == 200
    assert resp["body"]["net_cents"] == 600
    assert resp["body"]["reconciled"] is True
