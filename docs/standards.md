# Development Standards and Conventions

## 1. Coding standards
- Use TypeScript for the web app and extension.
- Use Python for the backend with strict typing.
- Prefer clear, descriptive names over abbreviations.
- Keep functions small and focused on one responsibility.
- Use domain-driven naming for modules and services.

## 2. Naming conventions
### TypeScript and React
- Components: PascalCase, e.g. ProfileCard.
- Hooks: useXxx.
- Utility modules: camelCase.
- Constants: UPPER_SNAKE_CASE.

### Python
- Modules: snake_case.
- Classes: PascalCase.
- Functions and variables: snake_case.
- Constants: UPPER_SNAKE_CASE.

## 3. Architecture conventions
- Organize by feature and domain, not by technical layer alone.
- Keep infrastructure concerns isolated from business logic.
- Define interfaces for external services and storage adapters.
- Favor explicit data contracts over loosely defined payloads.

## 4. Validation and error handling
- Validate inbound payloads at the API boundary.
- Return consistent error envelopes.
- Log important failures with correlation identifiers.
- Avoid swallowing exceptions silently.

## 5. Git branching strategy
Use a lightweight Git flow model:
- main: production-ready code.
- develop: integration branch for upcoming work.
- feature/*: work for a single feature or story.
- fix/*: small bug fixes.
- hotfix/*: urgent production fixes.
- release/*: stabilization branch before deployment.

## 6. Pull request expectations
- Small, reviewable changes.
- Clear commit messages.
- Tests required for shared logic and critical paths.
- Documentation updated when behavior changes.
