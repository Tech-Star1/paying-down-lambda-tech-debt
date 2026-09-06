from session_handler import is_valid_session, lambda_handler


def test_valid_session_token():
    assert is_valid_session("sess_12345678") is True


def test_invalid_session_tokens():
    assert is_valid_session("sess_123") is False
    assert is_valid_session("bad") is False
    assert is_valid_session("") is False


def test_lambda_handler_status():
    assert lambda_handler({"session_token": "sess_00000001"}, None)["statusCode"] == 200
    assert lambda_handler({"session_token": "nope"}, None)["statusCode"] == 400
