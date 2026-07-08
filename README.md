# GoJob

GoJob is a production-ready SaaS platform for AI-assisted career growth. The system combines a web dashboard for job seekers with a Chrome extension that can assist with application form completion after user review.

This milestone focuses on environment scaffolding and developer experience. Authentication and AI features are intentionally not implemented yet.

## Monorepo structure
- apps/web: Next.js 15 dashboard experience
- apps/api: FastAPI backend API
- apps/extension: Chrome extension shell
- packages/ui: shared UI primitives
- packages/shared: shared contracts and utilities
- packages/database: persistence scaffolding
- docs: architecture and planning documents

## Architectural decisions
- pnpm workspaces are used to keep dependencies and scripts consistent across apps and packages.
- The backend uses a modular FastAPI layout with a clear core and domain boundary.
- The web app uses the App Router so the dashboard can grow without a monolithic route tree.
- The extension uses Vite and React for a lightweight, MV3-friendly development loop.
- Docker Compose provides PostgreSQL and Redis for local development without coupling the environment to host installs.
- Environment variables are centralized through root and app-level example files.

## Development commands
1. Install pnpm if needed: `corepack enable`
2. Install dependencies: `pnpm install`
3. Start PostgreSQL and Redis: `docker compose up -d postgres redis`
4. Start the full development stack: `pnpm dev`

## Individual app commands
- Web app: `pnpm --filter @gojob/web dev`
- API: `pnpm --filter @gojob/api dev`
- Extension: `pnpm --filter @gojob/extension dev`
