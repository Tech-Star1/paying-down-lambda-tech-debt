# Batch: ledger-service (PCI-scoped)

The PCI-scoped domain, the one you modernize-as-you-migrate for a PCI
lift-and-shift. Four handlers on `python3.10`. Tests green on a **Python 3.10
baseline**. This batch deliberately **reuses idioms** seen in other domains to
make a point: the same debt recurs across every account, and the batching
model handles it consistently.

## Idiom manifest

| Handler | Seeded idiom | Status by 3.13 | Notes |
|---------|--------------|----------------|-------|
| `posting_handler.py` | `datetime.utcfromtimestamp()` | Deprecated (3.12) | **PARITY GATE #2** - exact naive audit timestamp; naive fix adds `+00:00` and trips |
| `balance_handler.py` | `distutils.util.strtobool` | **Removed (3.12)** | Recurs from payments (same debt, different account) |
| `audit_handler.py` | invalid escape sequence | SyntaxWarning (3.12) | Recurs from identity (lint-level debt is everywhere) |
| `statement_handler.py` | `typing.List` / `typing.Optional` | Not removed (soft) | Modernize to builtins / `X | None` |

## Watch the gate

`posting_handler.py` is the second seeded trust case, in the PCI domain where
it matters most. Its test asserts the **exact naive-UTC** audit timestamp. A
transform that makes the timestamp timezone-aware changes the audit string and
**fails validation**. That is the compliance beat: silent format drift in a
PCI audit trail is caught, not shipped.

## Run this batch

```bash
cd ledger-service
python -m pytest -q          # baseline on Python 3.10
atx custom def exec -p ./src -n AWS/python-version-upgrade \
  -c "python -m pytest -q" \
  --configuration "additionalPlanContext=The target Python version to upgrade to is Python 3.13" -x -t
git diff <base>..HEAD
python -m py_compile src/*.py && python -m pytest -q   # after, on Python 3.13
```
