from posting_handler import post_entry, lambda_handler

# Parity gate #2: exact naive-UTC audit timestamp, no offset suffix.


def test_post_entry_naive_timestamp():
    rec = post_entry("GL-000001", 15000, 0)
    assert rec["posted_at"] == "1970-01-01T00:00:00"
    assert "+" not in rec["posted_at"]


def test_lambda_handler_posts_entry():
    resp = lambda_handler({"entry_id": "GL-000002", "amount_cents": 9900, "epoch": 0}, None)
    assert resp["statusCode"] == 200
    assert resp["body"]["posted_at"] == "1970-01-01T00:00:00"
    assert "+" not in resp["body"]["posted_at"]
