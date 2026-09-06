from login_handler import verify_credentials, lambda_handler


def test_verify_credentials_ok():
    assert verify_credentials("alice", "hunter2!") is True


def test_verify_credentials_short_password():
    assert verify_credentials("alice", "short") is False


def test_verify_credentials_empty_user():
    assert verify_credentials("", "longenough") is False


def test_lambda_handler_status():
    assert lambda_handler({"username": "bob", "password": "password1"}, None)["statusCode"] == 200
    assert lambda_handler({"username": "bob", "password": "x"}, None)["statusCode"] == 401
