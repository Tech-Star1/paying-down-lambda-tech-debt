# Batch: notifications-service

Scoping unit for one `atx` run. Four handlers on `python3.10`, idiom spread
again distinct from prior batches. Tests green on a **Python 3.10 baseline**.

## Idiom manifest

| Handler | Seeded idiom | Status by 3.13 | Notes |
|---------|--------------|----------------|-------|
| `email_handler.py` | `imghdr` module | **Removed (3.13)** | Fix: content-type check / file-type lib; untested path |
| `sms_handler.py` | `datetime.utcfromtimestamp()` | Deprecated (3.12) | Fix: `fromtimestamp(epoch, tz=timezone.utc)`; still present |
| `push_handler.py` | `pipes` module | **Removed (3.13)** | Fix: `shlex.quote`; untested path |
| `digest_handler.py` | `locale.getdefaultlocale()` | Deprecated (3.11) | Fix: `setlocale`/`getlocale`; env-dependent, not asserted |

## Run this batch

```bash
cd notifications-service
python -m pytest -q          # baseline on Python 3.10
atx custom def exec -p ./src -n AWS/python-version-upgrade \
  -c "python -m pytest -q" \
  --configuration "additionalPlanContext=The target Python version to upgrade to is Python 3.13" -x -t
git diff <base>..HEAD
python -m py_compile src/*.py && python -m pytest -q   # after, on Python 3.13
```
