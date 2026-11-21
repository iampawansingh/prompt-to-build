# Placement Application Tracker

Student starter for **Prompt to Build**, facilitated by Pawan Kumar Singh at
Alliance University on 4 December 2026.

This local Python app uses Streamlit for the browser interface and SQLite for
persistence. The supplied starter initialises a database and displays six fictional
applications. You will build the entry form, validation, saving and editing during
the workshop; search, filters and progress counts follow the working core.

## Get started

- Follow [SETUP.md](SETUP.md) to install Git and uv, clone this repository and run the app.
- Open the cloned `prompt-to-build` folder in VS Code.
- Use `uv sync --locked` to prepare Python and dependencies.
- Run `uv run --locked streamlit run app.py --server.address localhost`.
- Expect six sample rows on the first run and the same rows after restart.

## Read the code

| File | Purpose |
| --- | --- |
| `app.py` | Streamlit page and sample table |
| `db.py` | SQLite connections, schema, sample initialisation and queries |
| `sample_data.json` | Six fictional application records |
| `check_setup.py` | Read-only readiness check |
| `pyproject.toml` | Project dependency declaration |
| `.python-version` | Python version selected by uv |
| `uv.lock` | Locked dependency versions |
| `requirements.txt` | Matching direct dependency pin for other tooling |

Start with `app.py`, then trace `db.init_db()` and `db.list_applications()`.
The first run creates `data/applications.db`. Sample rows are inserted only once
per database. Keep local environments and database files out of commits.

## Record your work

- Keep [ATTRIBUTION.md](ATTRIBUTION.md) and distinguish supplied code, your changes and AI assistance.
- Add features in small stages and verify each change against the code and executable checks.
- Publish your workshop work in your own repository when instructed; keep the starter attribution.
- Update your README with features you actually completed, setup instructions, sample output, checks and limitations.

The supplied code supports sample viewing only. It is a local, single-user learning
project; it does not include authentication, deployment or background reminders.
