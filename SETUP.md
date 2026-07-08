# GoJob Setup Guide

This guide is intended for a fresh clone of the repository. The goal is to make the development environment reproducible before product features are added.

## 1. Required software

Use the following versions as the baseline for local development:

- Node.js 20.x or 22.x
- pnpm 9.x
- Python 3.11+
- uv 0.4+ (recommended for the API workspace)
- Docker Desktop 4.x+
- PostgreSQL 16+
- Redis 7+

A Node version file is included at [.nvmrc](.nvmrc).

## 2. Installation

### macOS / Linux

```bash
corepack enable
pnpm install
```

### Windows PowerShell

```powershell
corepack enable
pnpm install
```

### Python environment for the API

The API workspace includes a Python dependency file. If you have uv installed, use:

```bash
cd apps/api
uv venv
uv pip install -r requirements.txt
```

If uv is not available, install the requirements with pip:

```bash
cd apps/api
py -3 -m pip install -r requirements.txt
```

## 3. Environment variables

Create a root environment file from the example template:

```bash
cp .env.example .env
```

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

The root environment file contains:

- Required now: `APP_ENV`, `DATABASE_URL`, `REDIS_URL`, `NEXT_PUBLIC_API_URL`, `VITE_API_BASE_URL`, `JWT_SECRET`, `JWT_REFRESH_SECRET`
- Placeholders for future features: `OPENAI_API_KEY`, `STORAGE_*`, `SMTP_*`, `SENTRY_DSN`, `OTEL_EXPORTER_OTLP_ENDPOINT`

## 4. Start PostgreSQL and Redis

Using Docker Compose:

```bash
docker compose up -d postgres redis
```

The API expects PostgreSQL and Redis to be reachable at the defaults defined in the environment file.

## 5. Start the applications

### Web app

```bash
pnpm --filter @gojob/web dev
```

Open http://localhost:3000

### API

```bash
cd apps/api
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Or with the workspace script:

```bash
pnpm --filter @gojob/api dev
```

Open http://localhost:8000/health

### Extension

```bash
pnpm --filter @gojob/extension dev
```

Open the Vite preview at http://localhost:5173

## 6. Docker setup

To build and run the containerized development stack:

```bash
docker compose -f docker-compose.dev.yml up --build
```

This starts the web app, API, and extension containers together.

## 7. Database initialization

The backend uses Alembic for schema migration management. After the PostgreSQL container is running:

```bash
cd apps/api
alembic upgrade head
```

If migrations are not created yet, the current scaffold still supports the database connection configuration and health inspection path.

## 8. Useful scripts

From the repository root:

```bash
pnpm dev
pnpm build
pnpm lint
pnpm test
```

## 9. Troubleshooting

### pnpm is not found

```bash
corepack enable
npm install -g pnpm@9.15.0
```

### Python is not available on Windows

Use the launcher explicitly:

```powershell
py -3 --version
```

### PostgreSQL connection errors

- Confirm Docker is running.
- Confirm the container is healthy.
- Verify `DATABASE_URL` in your `.env` file.

### Port conflicts

If port 3000, 8000, 5173, 5432, or 6379 is already in use, stop the conflicting process or change the port in the relevant config.

### API dependencies cannot be installed

If network access is restricted, use an internal package mirror or install the dependencies from your organization’s approved source.

## 10. Remaining blockers before authentication work

The following items still need attention before authentication features are implemented:

- The API runtime depends on a working Python environment in the target developer machine.
- The database schema is still scaffolded and not yet wired to a full migration set.
- The backend auth layer, session model, and password handling are not implemented yet.
- The environment file should be copied to a real `.env` file before running local services.
- Optional integrations such as object storage, email, and AI providers remain placeholders.
