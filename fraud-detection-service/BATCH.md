# Batch: fraud-detection-service (provided.al2 custom runtime)

The architecturally distinct domain. These functions run on the **custom
`provided.al2` runtime** (Amazon Linux 2), not a managed python3.x runtime.
`provided.al2` is itself end-of-support, so this is a **different AWS Transform
scenario**: the runtime interface (`bootstrap`) AND the Python code both move.
Migration target is a managed `python3.13` runtime (or `provided.al2023` as a
minimum interim step).

Three handlers + a `bootstrap` runtime loop. Tests green on a **Python 3.10
baseline**.

## Idiom manifest

| Handler | Seeded idiom | Status by 3.13 | Notes |
|---------|--------------|----------------|-------|
| `score_handler.py` | `@asyncio.coroutine` | **Removed (3.11)** | Fix: `async def`; two moving parts with the runtime migration |
| `rules_handler.py` | `distutils.version.LooseVersion` | **Removed (3.12)** | Fix: `packaging.version.Version` |
| `watchlist_handler.py` | `typing.List` | Not removed (soft) | Modernize to builtin generics |
| `bootstrap` | custom `provided.al2` runtime loop | AL2 end-of-support | The runtime interface itself is the migration |

## The demo beat this domain unlocks

The managed domains answer "upgrade my Python version." This one answers "and
what about my **custom runtime** functions?" Same assess -> plan -> validate ->
review model, harder starting point. Good for showing Transform is not just a
version-bumper.

## Run this batch

```bash
cd fraud-detection-service
python -m pytest -q          # baseline on Python 3.10
atx custom def exec -p ./src -n AWS/python-version-upgrade \
  -c "python -m pytest -q" \
  --configuration "additionalPlanContext=Migrate from the provided.al2 custom runtime to a managed Python 3.13 runtime" -x -t
git diff <base>..HEAD
python -m py_compile src/*.py && python -m pytest -q   # after, on Python 3.13
```
