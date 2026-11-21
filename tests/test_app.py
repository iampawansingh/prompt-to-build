"""Run the Streamlit starter with isolated data and no browser dependency."""

from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from streamlit.testing.v1 import AppTest

from placement_tracker import config, database


APP_FILE = Path(__file__).resolve().parents[1] / "src" / "placement_tracker" / "app.py"


class StarterAppTests(unittest.TestCase):
    def test_sample_table_and_empty_state(self):
        with tempfile.TemporaryDirectory() as temp:
            db_path = Path(temp) / "applications.db"
            with patch.object(config, "DB_PATH", db_path):
                app = AppTest.from_file(str(APP_FILE), default_timeout=20).run()
                self.assertFalse(app.exception)
                self.assertEqual(app.title[0].value, "Placement Application Tracker")
                self.assertEqual(len(app.dataframe[0].value), 6)
                app.run()
                self.assertFalse(app.exception)
                self.assertEqual(len(database.list_applications(db_path)), 6)

                with database.connection(db_path) as conn:
                    conn.execute("DELETE FROM applications")
                empty = AppTest.from_file(str(APP_FILE), default_timeout=20).run()
                self.assertFalse(empty.exception)
                self.assertEqual(len(empty.dataframe), 0)
                self.assertTrue(any(item.value == "No applications yet." for item in empty.info))


if __name__ == "__main__":
    unittest.main()
