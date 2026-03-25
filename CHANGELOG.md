# Changelog

All notable changes to this project will be documented here.

Format: [Semantic Versioning](https://semver.org)

---

## [1.0.0] — 2026-03-24

### Added
- **6 agents** — `fastapi-architect`, `api-implementer`, `async-reviewer`, `migration-guard`, `pr-reviewer`, `architecture-enforcer`
- **7 commands** — `/design-api`, `/implement-api`, `/review-async`, `/check-migration`, `/plan-feature`, `/review-api`, `/refactor`
- **4 skills** — `fastapi-architecture`, `sqlalchemy-async`, `alembic-safety`, `rest-response-standard`
- **`/refactor` wow feature** — paste any messy FastAPI file, get back clean architecture split across correct layers with async issues fixed
- **`architecture-enforcer` agent** — layer mapping + full refactor output in structured format
- **Example app** — full FastAPI app with users, projects, subscriptions, notifications, real Alembic migration
- **Before/after demo** — `bad_projects_router.py` → `clean_projects_router.py` with annotated walkthrough
- **Install script** — `install.sh` and `install.py` with `--dir` and `--merge` flags
- Strict repeatable output formats on all commands
