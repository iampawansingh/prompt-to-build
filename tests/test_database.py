"""Exercise the starter's real SQLite behaviour in disposable databases."""

from pathlib import Path
import os
import sqlite3
import subprocess
import sys
import tempfile
import unittest

from placement_tracker import config, database


class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.db_path = Path(self.temp.name) / "nested" / "applications.db"

    def test_initialisation_seeds_only_once(self):
        database.init_db(self.db_path)
        first = database.list_applications(self.db_path)
        self.assertEqual(len(first), 6)
        self.assertEqual(first[0]["company"], "Fern Software")
        self.assertEqual(first[-1]["company"], "Aster Labs")
        self.assertEqual(
            {status: sum(row["status"] == status for row in first)
             for status in config.STATUSES},
            {"Draft": 1, "Applied": 2, "Interview": 1, "Offer": 1, "Rejected": 1},
        )
        database.init_db(self.db_path)
        self.assertEqual(database.list_applications(self.db_path), first)

    def test_saved_data_survives_a_new_process_and_another_working_directory(self):
        database.init_db(self.db_path)
        with database.connection(self.db_path) as conn:
            conn.execute(
                """INSERT INTO applications
                   (company, role, application_date, status) VALUES (?, ?, ?, ?)""",
                ("O'Neil Labs", "Python Intern", "2026-12-04", "Applied"),
            )
        env = {**os.environ, "PTB_DB_PATH": str(self.db_path)}
        result = subprocess.check_output(
            [sys.executable, "-c",
             "from placement_tracker import database; database.init_db(); "
             "rows = database.list_applications(); "
             "assert len(rows) == 7; print(rows[0]['company'])"],
            cwd=self.temp.name,
            env=env,
            text=True,
        )
        self.assertEqual(result.strip(), "O'Neil Labs")

    def test_failed_write_rolls_back_and_connection_closes(self):
        database.init_db(self.db_path)
        with self.assertRaises(sqlite3.IntegrityError):
            with database.connection(self.db_path) as conn:
                conn.execute("UPDATE applications SET notes = ? WHERE id = ?", ("Uncommitted", 1))
                conn.execute("UPDATE applications SET status = ? WHERE id = ?", ("Invalid", 1))
        row = next(row for row in database.list_applications(self.db_path) if row["id"] == 1)
        self.assertEqual(row["notes"], "Fictional sample application")
        with self.assertRaises(sqlite3.ProgrammingError):
            conn.execute("SELECT 1")

    def test_intentionally_empty_database_is_not_reseeded(self):
        database.init_db(self.db_path)
        with database.connection(self.db_path) as conn:
            conn.execute("DELETE FROM applications")
        database.init_db(self.db_path)
        self.assertEqual(database.list_applications(self.db_path), [])


if __name__ == "__main__":
    unittest.main()
