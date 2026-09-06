# Batch: payments-service

Scoping unit for one `atx` run. Five handlers on `python3.10`, each carrying a
distinct deprecation so the run teaches the full range. All tests are green on
a **Python 3.10 baseline** before transformation.

## Idiom manifest

| Handler | Seeded idiom | Status by 3.13 | Behavior-safe transform? |
|---------|--------------|----------------|--------------------------|
| `charge_handler.py` | `datetime.utcnow()` | Deprecated (3.12), still present | Yes (tested surface is fee math) |
| `refund_handler.py` | `distutils.util.strtobool` | **Removed (3.12)** | Yes (swap for a local bool parser) |
| `payout_handler.py` | `imp` module | **Removed (3.12)** | Yes (swap for `importlib`) |
| `settlement_handler.py` | `cgi` module | **Removed (3.13)** | Yes (swap for `email.message` / `urllib.parse`) |
| `reconcile_handler.py` | `datetime.utcnow().isoformat()` | Deprecated (3.12) | **NO - strict-parity gate** |

## Watch the gate

`reconcile_handler.py` is the seeded trust case. Its test asserts the **exact
naive-UTC** timestamp string (no `+00:00` offset). The obvious modernization
(`datetime.now(timezone.utc)`) changes that string and **fails validation**,
routing the change back. The behavior-preserving fix keeps the naive format
explicitly. Watch which one the agent produces - that failure-routes-back
moment is the compliance beat for the room.

## Interpreter requirement (important)

Three idioms here (`distutils`, `imp`, `cgi`) are **removed** by 3.12/3.13, so
they only import on an older interpreter. To show a true "green before -> green
after":

- Baseline (before): run tests on **Python 3.10** (a `pyenv`/venv 3.10).
- After transform: run tests on **Python 3.13**.

If you run the baseline on 3.13, the removed-module imports fail - that is the
debt, not a repo bug.

## Run this batch

```bash
cd payments-service

# baseline (on Python 3.10)
python -m pytest -q

atx custom def list
atx custom def exec \
  -p ./src \
  -n AWS/python-version-upgrade \
  -c "python -m pytest -q" \
  --configuration "additionalPlanContext=The target Python version to upgrade to is Python 3.13" \
  -x -t

git log --oneline
git diff <base>..HEAD
python -m py_compile src/*.py
python -m pytest -q          # after transform, on Python 3.13
```
