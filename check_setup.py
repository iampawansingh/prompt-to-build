"""Run with the same interpreter that will run the app. Does not create a DB."""
import importlib.metadata
import sqlite3
import sys
from pathlib import Path

print("Interpreter:", sys.executable)
print("Python:", sys.version.split()[0])
print("SQLite:", sqlite3.sqlite_version)
assert (3, 11) <= sys.version_info[:2] <= (3, 15), "Use supported Python 3.11 to 3.15; prefer 3.12 for this workshop."
print("Streamlit:", importlib.metadata.version("streamlit"))
assert importlib.metadata.version("streamlit") == "1.67.0", "Run uv sync --locked."
for name in ("app.py", "db.py", "sample_data.json", "pyproject.toml", ".python-version", "uv.lock"):
    assert (Path(__file__).parent / name).is_file(), f"Missing {name}"
print("Readiness checks passed. Next: uv run --locked streamlit run app.py --server.address localhost")
