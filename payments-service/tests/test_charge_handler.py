from charge_handler import calculate_charge, lambda_handler


def test_calculate_charge_math():
    # 2.9% of 10000 = 290, + 30 flat = 320 fee
    result = calculate_charge(10000)
    assert result == {"gross_cents": 10000, "fee_cents": 320, "net_cents": 9680}


def test_lambda_handler_returns_net_and_timestamp():
    resp = lambda_handler({"amount_cents": 5000}, None)
    assert resp["statusCode"] == 200
    # 2.9% of 5000 = 145, + 30 = 175 fee
    assert resp["body"]["fee_cents"] == 175
    assert resp["body"]["net_cents"] == 4825
    # timestamp present but format is not asserted here (see reconcile for parity)
    assert "processed_at" in resp["body"]
