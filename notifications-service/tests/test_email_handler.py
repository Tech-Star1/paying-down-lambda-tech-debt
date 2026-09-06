from email_handler import is_allowed, lambda_handler


def test_is_allowed_image_extensions():
    assert is_allowed("photo.png") is True
    assert is_allowed("SCAN.JPG") is True


def test_is_allowed_rejects_others():
    assert is_allowed("report.pdf") is False
    assert is_allowed("") is False


def test_lambda_handler_status():
    assert lambda_handler({"filename": "a.gif"}, None)["statusCode"] == 200
    assert lambda_handler({"filename": "a.exe"}, None)["statusCode"] == 415
