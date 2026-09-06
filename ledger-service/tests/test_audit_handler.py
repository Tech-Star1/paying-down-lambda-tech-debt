from audit_handler import is_valid_ref, lambda_handler


def test_valid_ref():
    assert is_valid_ref("GL-123456") is True


def test_invalid_refs():
    assert is_valid_ref("GL-123") is False
    assert is_valid_ref("XX-123456") is False
    assert is_valid_ref("") is False


def test_lambda_handler_status():
    assert lambda_handler({"ref": "GL-000001"}, None)["statusCode"] == 200
    assert lambda_handler({"ref": "bad"}, None)["statusCode"] == 400
