"""Shared settings for the local workshop application."""

import os
from pathlib import Path

# This application runs from a source checkout installed by `uv sync`.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DB_PATH = Path(
    os.environ.get("PTB_DB_PATH", PROJECT_ROOT / "data" / "applications.db")
).expanduser()

STATUSES = ("Draft", "Applied", "Interview", "Offer", "Rejected")
