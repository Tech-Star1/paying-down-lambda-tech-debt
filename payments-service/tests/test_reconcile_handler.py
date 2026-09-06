"""Strict behavior-parity gate for the reconciliation timestamp.

The contract: reconciled_at is a NAIVE UTC ISO-8601 string with NO offset
suffix. A modernization that swaps datetime.utcnow() for
datetime.now(timezone.utc) makes the value timezone-aware and isoformat()
appends '+00:00', breaking these assertions. That is the gate doing its job:
a behavior-changing transform fails validation and routes back.
"""
import reconcile_handler
from datetime import datetime
from reconcile_handler import reconcile, lambda_handler

FIXED = datetime(2026, 1, 15, 8, 30, 0)  # naive UTC, injected for determinism


def test_reconcile_exact_naive_isoformat():
    record = reconcile("txn_1", 9680, FIXED)
    assert record["reconciled_at"] == "2026-01-15T08:30:00"
    assert "+" not in record["reconciled_at"]  # parity invariant: no tz offset


def test_lambda_handler_timestamp_is_naive(monkeypatch):
    class _FrozenClock:
        @staticmethod
        def utcnow():
            return FIXED

    monkeypatch.setattr(reconcile_handler, "datetime", _FrozenClock)
    resp = lambda_handler({"txn_id": "txn_1", "amount_cents": 9680}, None)
    assert resp["statusCode"] == 200
    assert resp["body"]["reconciled_at"] == "2026-01-15T08:30:00"
    assert "+" not in resp["body"]["reconciled_at"]
