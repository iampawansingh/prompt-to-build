"""Check the source checkout without creating or changing its database."""

import importlib.metadata
from pathlib import Path
import sqlite3
import sys

import placement_tracker


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def main():
    print("Interpreter:", sys.executable)
    print("Python:", sys.version.split()[0])
    print("SQLite:", sqlite3.sqlite_version)
    if not (3, 11) <= sys.version_info[:2] <= (3, 15):
        raise SystemExit("Use supported Python 3.11 to 3.15; prefer 3.12.")

    version = importlib.metadata.version("streamlit")
    print("Streamlit:", version)
    if version != "1.67.0":
        raise SystemExit("Run uv sync --locked to install the workshop dependencies.")

    required_files = (
        "src/placement_tracker/app.py",
        "src/placement_tracker/database.py",
        "src/placement_tracker/config.py",
        "src/placement_tracker/resources/sample_applications.json",
        "pyproject.toml",
        ".python-version",
        "uv.lock",
    )
    for name in required_files:
        if not (PROJECT_ROOT / name).is_file():
            raise SystemExit(f"Missing {name}. Run from a complete repository clone.")

    expected_package = PROJECT_ROOT / "src" / "placement_tracker" / "__init__.py"
    if Path(placement_tracker.__file__).resolve() != expected_package.resolve():
        raise SystemExit("Package points to another checkout. Run uv sync --locked here.")
    print("Package:", placement_tracker.__file__)
    print("Readiness checks passed.")
    print("Next: uv run --locked streamlit run src/placement_tracker/app.py --server.address localhost")


if __name__ == "__main__":
    main()
