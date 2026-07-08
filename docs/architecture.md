# Alvest AI Architecture Plan

## 1. Product architecture overview
Alvest AI will be delivered as a monorepo with three user-facing applications:
- A web application for account management, resume analysis, job matching, and application tracking.
- A FastAPI backend that exposes secure domain services and AI workflows.
- A Chrome extension that helps users complete job applications on supported websites after review.

The architecture should prioritize:
- Clear domain boundaries.
- Type-safe contracts between layers.
- Asynchronous AI processing for long-running tasks.
- Strong security and auditability.

## 2. Recommended stack refinements
The proposed stack is strong, but a few additions will improve production readiness:
- Add object storage such as S3-compatible storage for resume files and generated documents.
- Add a task queue such as Celery, RQ, or Arq backed by Redis for resume parsing, matching, and AI generation.
- Add structured logging, tracing, and error monitoring with OpenTelemetry and Sentry.
- Add rate limiting, audit logging, and abuse protection at the API layer.
- Add pgvector or a similar vector store once semantic search becomes a priority.
- Generate OpenAPI contracts and SDKs from the backend to keep the web app and extension aligned.

## 3. Monorepo structure
```text
apps/
  web/
  api/
  extension/
packages/
  ui/
  shared/
  database/
docs/
```

## 4. Responsibility of each folder
- apps/web: Next.js dashboard, authentication flows, profile management, dashboard experiences, and AI-driven views.
- apps/api: FastAPI services, domain logic, AI orchestration, persistence, authentication, and integrations.
- apps/extension: Manifest V3 extension UI, content scripts, background worker, and job application assistance flows.
- packages/ui: shared UI primitives, design-system components, and layout patterns.
- packages/shared: common types, API contracts, validation helpers, constants, and utility logic.
- packages/database: SQLAlchemy models, migrations, and database bootstrapping logic.
- docs: architecture documents, standards, API notes, and roadmap material.

## 5. Target application architecture
### Web app
- Next.js 15 App Router.
- Server components for read-only views and lightweight data hydration.
- Client components for interactive workflows such as forms, file upload, and dashboard state.
- A typed API client generated from backend contracts.

### API backend
- FastAPI with modular feature-based packages.
- Pydantic validation for request and response models.
- SQLAlchemy for persistence.
- Alembic for migrations.
- Redis-backed queues for asynchronous AI work.
- JWT access/refresh tokens with secure cookie or bearer token handling.

### Chrome extension
- MV3 background service worker for orchestration.
- Content scripts for supported domains.
- Popup and options pages for user review and settings.
- Secure messaging bridge between the extension and the backend.

## 6. API module structure
The backend should be organized around business domains rather than a single large app file.

```text
apps/api/src/
  main.py
  core/
    config/
    security/
    errors/
    logging/
  modules/
    auth/
    users/
    profiles/
    resumes/
    ai/
    jobs/
    applications/
    cover_letters/
    screening_answers/
    integrations/
  shared/
    schemas/
    services/
    events/
  infrastructure/
    db/
    storage/
    redis/
    workers/
```

## 7. Frontend module structure
The web app should follow feature-oriented organization.

```text
apps/web/src/
  app/
    (public)/
    (dashboard)/
  components/
    ui/
    layout/
  features/
    auth/
    profile/
    resumes/
    jobs/
    applications/
    ai/
  lib/
    api/
    auth/
    utils/
  styles/
```

## 8. Chrome extension architecture
```text
apps/extension/src/
  background/
  content/
  popup/
  options/
  shared/
    messaging/
    types/
    storage/
```

Responsibilities:
- background: service worker lifecycle, token refresh, message handling.
- content: page-aware injection on supported websites.
- popup: review and approval UI for assisted form filling.
- options: extension settings and connection state.
- shared: message contracts and common utilities.

## 9. Environment variables
The initial environment model should be explicit and centralized.

### Shared
- APP_ENV
- APP_NAME
- APP_BASE_URL
- FRONTEND_URL
- API_BASE_URL
- JWT_SECRET
- JWT_REFRESH_SECRET

### Backend
- DATABASE_URL
- REDIS_URL
- OPENAI_API_BASE_URL
- OPENAI_API_KEY
- OPENAI_MODEL
- STORAGE_ENDPOINT
- STORAGE_ACCESS_KEY
- STORAGE_SECRET_KEY
- STORAGE_BUCKET
- STORAGE_PUBLIC_URL
- SMTP_HOST
- SMTP_PORT
- SMTP_USER
- SMTP_PASSWORD

### Frontend
- NEXT_PUBLIC_API_URL
- NEXT_PUBLIC_APP_ENV
- NEXT_PUBLIC_EXTENSION_ID

### Extension
- VITE_API_BASE_URL
- VITE_EXTENSION_ENV

## 10. Initial database entities (high level)
- User
- UserProfile
- Resume
- ResumeAnalysis
- JobPosting
- JobMatch
- Application
- CoverLetterDraft
- ScreeningAnswerDraft
- CompanyProfile
- AuditEvent
- RefreshToken

These entities should be designed with clear ownership and lifecycle states.

## 11. Core product flows
1. User registers and authenticates.
2. User creates or updates a profile.
3. User uploads one or more resumes.
4. Backend parses and analyzes the resume.
5. Backend matches the resume to roles and suggests opportunities.
6. User generates cover letters and screening answers.
7. User tracks applications and review status.
8. Extension assists with form completion on supported sites after explicit review.

## 12. Security and compliance expectations
- Enforce role-based access where relevant.
- Store secrets in environment-based secret managers.
- Encrypt sensitive documents at rest and in transit.
- Keep audit logs for important actions.
- Require explicit user approval for extension-assisted form filling.

## 13. Implementation principles
- Feature-based module organization.
- Strong typing across web, API, and extension.
- Explicit interfaces between domain and infrastructure layers.
- API contracts validated in both frontend and backend.
- Favor composition over deep inheritance.
- Keep business rules inside domain services.
