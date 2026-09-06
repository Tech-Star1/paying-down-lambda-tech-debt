# Batch: identity-service

Scoping unit for one `atx` run. Four handlers on `python3.10`, distinct idiom
spread from payments so the run teaches new cases. Tests green on a
**Python 3.10 baseline**.

## Idiom manifest

| Handler | Seeded idiom | Status by 3.13 | Notes |
|---------|--------------|----------------|-------|
| `login_handler.py` | `asyncio.get_event_loop()` (no running loop) | Deprecated (3.10+) | Modern form is `asyncio.run()` |
| `session_handler.py` | invalid escape sequence in a plain string (`"\d"`) | SyntaxWarning (3.12) | Fix is a raw string `r"..."` |
| `token_handler.py` | `typing.List` / `typing.Dict` | Not removed (soft) | Modernize to builtin generics (`list`/`dict`, 3.9+) |
| `mfa_handler.py` | `ssl.wrap_socket()` | **Removed (3.12)** | Fix is `ssl.SSLContext.wrap_socket`; sits in an untested path |

Teaching value: two hard breaks (`ssl.wrap_socket`), a warning-only case
(`asyncio`), a lint-level case (invalid escape), and a "improve but not broken"
case (`typing`). Watch how the agent classifies and handles each severity.

## Run this batch

```bash
cd identity-service
python -m pytest -q          # baseline on Python 3.10
atx custom def exec -p ./src -n AWS/python-version-upgrade \
  -c "python -m pytest -q" \
  --configuration "additionalPlanContext=The target Python version to upgrade to is Python 3.13" -x -t
git diff <base>..HEAD
python -m py_compile src/*.py && python -m pytest -q   # after, on Python 3.13
```
