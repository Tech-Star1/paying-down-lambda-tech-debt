from mfa_handler import generate_challenge, lambda_handler


def test_generate_challenge_deterministic():
    assert generate_challenge("abc") == generate_challenge("abc")


def test_generate_challenge_format():
    challenge = generate_challenge("secret")
    assert challenge.startswith("mfa-")
    assert len(challenge) == 10  # 'mfa-' + 6 digits


def test_lambda_handler_returns_challenge():
    resp = lambda_handler({"secret": "topsecret"}, None)
    assert resp["statusCode"] == 200
    assert resp["body"]["challenge"].startswith("mfa-")
