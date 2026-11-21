"""Small local SQLite layer. Each function opens and closes its own connection."""
from contextlib import contextmanager
from importlib.resources import files
from pathlib import Path
import json
import sqlite3

from placement_tracker import config


@contextmanager
def connection(db_path=None):
    """Commit successful operations, roll back errors, and always close."""
    path = Path(db_path) if db_path is not None else config.DB_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path, timeout=10)
    conn.row_factory = sqlite3.Row
    try:
        with conn:
            yield conn
    finally:
        conn.close()


def init_db(db_path=None):
    """Create the schema and seed once. Reruns do not duplicate sample rows."""
    with connection(db_path) as conn:
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
            sample_file = files("placement_tracker").joinpath(
                "resources", "sample_applications.json"
            )
            rows = json.loads(sample_file.read_text(encoding="utf-8"))
            conn.executemany("""INSERT INTO applications
                (company, role, application_date, status, job_link, notes)
                VALUES (:company, :role, :application_date, :status, :job_link, :notes)""", rows)
            conn.execute("INSERT INTO metadata(key) VALUES (?)", ("seeded",))


def list_applications(db_path=None):
    """Return independent dictionaries sorted by ID, newest first."""
    with connection(db_path) as conn:
        return [dict(row) for row in conn.execute("SELECT * FROM applications ORDER BY id DESC")]

# Activity B2: add validation and add_application here.

# Activity B4: add update_application using a stable record ID here.
