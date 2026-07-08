# API - Database and Migrations

This document explains how to run database migrations for the `apps/api` service.

Prerequisites
- A running Postgres instance reachable from `DATABASE_URL`.
- Python 3.11+ and `pip`/`py` launcher available.
- Python dependencies installed (`pip install -r requirements.txt`).

Common commands (run from `apps/api`):

Create a virtualenv and install dependencies:

```bash
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1  # PowerShell
# or on macOS/Linux
source .venv/bin/activate

py -3 -m pip install -r requirements.txt
```

Apply migrations:

```bash
# ensure DATABASE_URL is set in the environment or in alembic.ini
alembic upgrade head
```

Autogenerate a new revision from model changes:

```bash
alembic revision --autogenerate -m "describe change"
```

Rollback one revision:

```bash
alembic downgrade -1
```

Notes
- `env.py` is configured to read `DATABASE_URL` from the environment and to import model metadata from `apps/api/src/models`.
- The initial migration `alembic/versions/0001_initial_schema.py` creates the core tables: `users`, `profiles`, `resumes`, `job_applications`.
# API Service

This package will host the FastAPI backend for GoJob.

Planned responsibilities:
- Authentication and authorization.
- Resume ingestion and analysis workflows.
- Job matching and drafting services.
- AI orchestration and integrations.
