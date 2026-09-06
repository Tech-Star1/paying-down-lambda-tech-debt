from sms_handler import format_sent_at, truncate, lambda_handler


def test_format_sent_at_epoch_zero():
    assert format_sent_at(0) == "1970-01-01T00:00:00"


def test_truncate_limits_to_160():
    assert truncate("x" * 200) == "x" * 160
    assert truncate("short") == "short"


def test_lambda_handler_body():
    resp = lambda_handler({"body": "hello", "epoch": 0}, None)
    assert resp["statusCode"] == 200
    assert resp["body"]["text"] == "hello"
    assert resp["body"]["sent_at"] == "1970-01-01T00:00:00"
