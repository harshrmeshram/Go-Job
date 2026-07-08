Alembic migration workflow

This folder contains Alembic configuration for the `apps/api` service.

Common commands (run from `apps/api`):

- Initialize the environment (already done in this repo):
  - `alembic init alembic` (not necessary; repo already has configuration)

- Create a new migration (autogenerate using models):
  - Ensure `PYTHONPATH=src` or run from `apps/api` with `src` on sys.path.
  - `alembic revision --autogenerate -m "add new tables"`

- Apply migrations to the database:
  - `alembic upgrade head`

- Downgrade:
  - `alembic downgrade -1`

Notes:
- The `env.py` is configured to import model metadata from `apps/api/src/models`.
- Make sure your `DATABASE_URL` in `.env` or `alembic.ini` points to a running Postgres instance.
- If `alembic` is not installed, install dependencies with:
  - `py -3 -m pip install -r requirements.txt`

*** End Patch