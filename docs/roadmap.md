# Development Roadmap

## Milestone 0 — Foundation
- Initialize the monorepo structure.
- Define architecture, contracts, and standards.
- Create environment configuration templates.
- Set up CI, linting, and formatting defaults.

## Milestone 1 — Authentication and onboarding
- User registration and login.
- Profile creation and account settings.
- Basic email verification and password reset.

## Milestone 2 — Resume management and AI analysis
- Resume upload and storage.
- Resume parsing and AI-based summaries.
- ATS scoring and keyword insights.

## Milestone 3 — Job matching and drafting
- Job discovery and matching workflow.
- Cover letter generation.
- Screening answer draft generation.

## Milestone 4 — Application tracking and extension
- Application tracking dashboard.
- Chrome extension MVP.
- Review-before-submit assistance workflow.

## Milestone 5 — Hardening and launch
- Performance tuning.
- Security audits.
- Observability and deployment readiness.
- Beta release and feedback loop.

## MVP TODO list
- Create account and login.
- Manage user profile.
- Upload and manage resumes.
- Analyze resumes with AI.
- Match resumes with jobs.
- Generate cover letters.
- Generate screening answer drafts.
- Track job applications.
- Support a basic extension-assisted review workflow.

## Technical risks and assumptions
- AI parsing quality may vary by resume format and source.
- Extension compatibility depends on website structure and DOM stability.
- Resume processing may be slower than real-time and should be asynchronous.
- Data privacy and document storage require careful design from day one.
- Assumption: the initial launch will target a single language locale and a defined set of supported websites.
