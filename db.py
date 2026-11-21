"""Small local SQLite layer. Each function opens and closes its own connection."""
from contextlib import contextmanager
from pathlib import Path
import json
import os
import sqlite3

ROOT = Path(__file__).resolve().parent
DB_PATH = Path(os.environ.get("PTB_DB_PATH", ROOT / "data" / "applications.db"))
STATUSES = ("Draft", "Applied", "Interview", "Offer", "Rejected")

@contextmanager
def connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH, timeout=10)
    conn.row_factory = sqlite3.Row
    try:
        with conn:
            yield conn
    finally:
        conn.close()

def init_db():
    """Create the schema and seed once. Reruns do not duplicate sample rows."""
    with connection() as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            application_date TEXT NOT NULL,
            status TEXT NOT NULL CHECK(status IN
                ('Draft', 'Applied', 'Interview', 'Offer', 'Rejected')),
            job_link TEXT NOT NULL DEFAULT '',
            notes TEXT NOT NULL DEFAULT ''
        )""")
        conn.execute("CREATE TABLE IF NOT EXISTS metadata (key TEXT PRIMARY KEY)")
        seeded = conn.execute("SELECT 1 FROM metadata WHERE key = ?", ("seeded",)).fetchone()
        if not seeded:
            rows = json.loads((ROOT / "sample_data.json").read_text(encoding="utf-8"))
            conn.executemany("""INSERT INTO applications
                (company, role, application_date, status, job_link, notes)
                VALUES (:company, :role, :application_date, :status, :job_link, :notes)""", rows)
            conn.execute("INSERT INTO metadata(key) VALUES (?)", ("seeded",))

def list_applications():
    """Return independent dictionaries sorted by ID, newest first."""
    with connection() as conn:
        return [dict(row) for row in conn.execute("SELECT * FROM applications ORDER BY id DESC")]

# Activity B2: add validation and add_application here.

# Activity B3: add update_application using a stable record ID here.
