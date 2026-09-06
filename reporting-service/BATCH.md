# Batch: reporting-service

Scoping unit for one `atx` run. Four handlers on `python3.10`. Tests green on a
**Python 3.10 baseline**.

## Idiom manifest

| Handler | Seeded idiom | Status by 3.13 | Notes |
|---------|--------------|----------------|-------|
| `export_handler.py` | `@asyncio.coroutine` decorator | **Removed (3.11)** | Fix: `async def`; applied at import, so module needs 3.10 |
| `version_handler.py` | `distutils.version.LooseVersion` | **Removed (3.12)** | Fix: `packaging.version.Version` |
| `aggregate_handler.py` | `collections.OrderedDict` | Not removed (soft) | Plain `dict` suffices since 3.7 |
| `render_handler.py` | `crypt` module | **Removed (3.13)** | Fix: `hashlib` / maintained lib; untested path |

## Run this batch

```bash
cd reporting-service
python -m pytest -q          # baseline on Python 3.10
atx custom def exec -p ./src -n AWS/python-version-upgrade \
  -c "python -m pytest -q" \
  --configuration "additionalPlanContext=The target Python version to upgrade to is Python 3.13" -x -t
git diff <base>..HEAD
python -m py_compile src/*.py && python -m pytest -q   # after, on Python 3.13
```
