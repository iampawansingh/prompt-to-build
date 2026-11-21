# Placement Application Tracker

Student starter for **Prompt to Build**, facilitated by Pawan Kumar Singh at
Alliance University on 4 December 2026.

This local Python app uses Streamlit for the browser interface and SQLite for
persistence. It initialises a database and displays six fictional applications.
During the workshop, you will add forms, validation, saving and editing, followed
by search, filters and progress counts.

## Get started

- Follow [the setup guide](docs/SETUP.md) to install Git and uv and clone the repository.
- Open the cloned `prompt-to-build` folder in VS Code and run these commands from its terminal:

  ```bash
  uv sync --locked
  uv run --locked python scripts/check_setup.py
  uv run --locked streamlit run src/placement_tracker/app.py --server.address localhost
  ```

- Expect six sample rows on the first run and the same rows after restart.

## Project layout

```text
prompt-to-build/
├── src/
│   └── placement_tracker/
│       ├── __init__.py
│       ├── app.py                    # Streamlit interface
│       ├── config.py                 # Database location and allowed statuses
│       ├── database.py               # SQLite access and initialisation
│       └── resources/
│           └── sample_applications.json
├── scripts/
│   └── check_setup.py                # Read-only readiness check
├── tests/
│   ├── test_database.py
│   └── test_app.py
├── docs/
│   ├── SETUP.md
│   └── ATTRIBUTION.md
├── pyproject.toml                    # Dependencies and package configuration
├── uv.lock                           # Locked dependency versions
├── .python-version                   # Python version selected by uv
└── requirements.txt                  # Direct dependency pin for other tooling
```

The app creates `data/applications.db` in the repository when it first runs.
That local database and `.venv/` are ignored by Git. Supplied sample data lives
inside the package under `resources/`; sample rows are inserted only once per
database. To use another database, set `PTB_DB_PATH` to its absolute file path
before starting the app.

## Read and extend the code

1. Begin with `src/placement_tracker/app.py` and its `main()` function.
2. Follow `database.init_db()` and `database.list_applications()` into `database.py`.
3. Read `config.py` to find the database location and supported statuses.
4. Compare the sample JSON with the table displayed in the browser.

Keep interface changes in `app.py`, database operations in `database.py`, and
shared settings in `config.py`. `uv sync` installs this source package in editable
mode, so edits under `src/` are used directly by the application.

## Verify your changes

```bash
uv run --locked python -m unittest discover -s tests -v
```

The starter checks cover sample initialisation, persistence in another process,
transaction rollback, closed connections and the Streamlit table and empty state.
They use temporary databases. Add checks for each capability you build, including
invalid input, restart persistence and editing one record without changing others.

## Record your work

- Keep [the contribution record](docs/ATTRIBUTION.md) and distinguish supplied code, your changes and AI assistance.
- Build in small stages and verify each change against source code and executable checks.
- Publish your workshop work in your own repository when instructed, with the starter attribution.
- Update your README with completed features, setup steps, sample output, checks and limitations.

The supplied code supports sample viewing only. It is a local, single-user learning
project without authentication, deployment or background reminders.
