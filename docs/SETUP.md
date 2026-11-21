# Setup and first run

## Before you start

- Bring a laptop, charger, browser and code editor such as VS Code.
- Install [Git](https://git-scm.com/install/) and check `git --version`.
- Keep internet available for setup, AI chat, GitHub and LinkedIn.
- `uv` manages Python 3.12, dependencies and the local environment; no manual activation is needed.
- SQLite is included with Python. No database server, API key or paid AI plan is required.

## Install uv once

- Windows PowerShell:

  ```powershell
  winget install --id=astral-sh.uv -e
  ```

- macOS or Linux terminal:

  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

- Reopen the terminal and run `uv --version`.
- If installation is blocked, ask college IT before workshop day; see the [official installation options](https://docs.astral.sh/uv/getting-started/installation/).

## Set up and run on any OS

- Clone the starter and enter its folder:

  ```bash
  git clone https://github.com/iampawansingh/prompt-to-build.git
  cd prompt-to-build
  ```

- Open this folder in VS Code, then run each command in its terminal:

  ```bash
  uv sync --locked
  uv run --locked python scripts/check_setup.py
  uv run --locked streamlit run src/placement_tracker/app.py --server.address localhost
  ```

- Open the printed URL, usually `http://localhost:8501`; keep the terminal running.
- Expect a passed readiness check and six fictional applications. The starter has no entry or edit form yet.
- Stop with Ctrl+C, repeat the last command and confirm the six rows remain.
- Use that same run command on later visits; begin reading `src/placement_tracker/app.py` and `database.py`.
- Sign into your AI chat service, GitHub and LinkedIn before arrival.
- Check the starter with `uv run --locked python -m unittest discover -s tests -v`.

## If something fails

- `uv` not found: reopen the terminal after installation.
- Missing files: open the terminal in `prompt-to-build`, beside `src/`, `pyproject.toml` and `uv.lock`.
- Dependency problem: rerun `uv sync --locked`; share the exact error with support.
- Port busy: append `--server.port 8502` to the run command.
- Database locked: stop duplicate app processes and close database viewers.
- Broken code: back up your edits and request a checkpoint; preserve your `data` folder.
- Keep `.venv` and database files local. Publish `pyproject.toml`, `.python-version` and `uv.lock` with your code.
