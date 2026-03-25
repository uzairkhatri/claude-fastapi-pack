# Claude FastAPI Pack

Plug-and-play Claude agents for FastAPI teams.

Design cleaner APIs, review async code, validate migrations, and ship backend features with production-ready structure.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Claude](https://img.shields.io/badge/Claude-Code-purple)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green)

---

<!-- ![Demo](assets/demo.gif) -->

---

## Why This Exists

Most Claude repos focus on prompts, notes, or generic best practices.

This repo is different.

`claude-fastapi-pack` gives backend developers a practical, opinionated Claude setup for real FastAPI work:
- architecture planning
- API design
- async code review
- migration safety checks
- production-minded implementation guidance

It is built for developers who want Claude to act like a **backend architect + reviewer**, not just a chatbot.

---

## What You Get

### Agents
Specialized Claude agents for FastAPI/backend workflows:
- `fastapi-architect`
- `api-implementer`
- `async-reviewer`
- `migration-guard`
- `pr-reviewer`
- `architecture-enforcer`

### Commands
Ready-to-run workflows:
- `/design-api`
- `/implement-api`
- `/review-async`
- `/check-migration`
- `/review-api`
- `/plan-feature`
- `/refactor`

### Skills
Reusable backend knowledge:
- FastAPI architecture
- SQLAlchemy async safety
- Alembic migration safety
- REST response standards

### Opinionated Standards
A base `CLAUDE.md` that pushes Claude toward:
- Router -> Service -> Model/Repository separation
- thin routes
- clean schemas
- safe async patterns
- production-safe migrations

---

## Who This Is For

This pack is for:
- FastAPI backend developers
- Python API teams
- SaaS teams building production systems
- developers using Async SQLAlchemy
- teams that want consistent architecture and better code review quality

This pack is **not** meant to be a generic AI prompt collection.

---

## Before vs After

**Before**
- route contains validation, business logic, DB query, and response shaping
- async issues ship silently until production load hits
- migrations run without safety review
- no consistent structure across the codebase

**After using Claude FastAPI Pack**
- route is thin — one service call, one return
- service owns all business logic
- schemas are explicit with typed request and response models
- async issues are caught before merge
- migration risks are identified before deployment
- every feature follows the same structure, regardless of who wrote it

---

## Core Philosophy

This repo assumes a clean backend structure:

- **Routes** handle HTTP concerns
- **Services** handle business logic
- **Schemas** validate and serialize
- **Models/Repositories** handle persistence
- **Migrations** are reviewed for safety before rollout

The goal is simple:

> Use Claude like a production backend teammate.

---

## Install

### Option A — copy the folder

```bash
cp -r .claude /your-project/
```

### Option B — one-line install

```bash
curl -sSL https://raw.githubusercontent.com/uzairkhatri/claude-fastapi-pack/main/install/install.sh | bash
```

```bash
python install/install.py
```

Both options copy agents, commands, and skills into your project's `.claude/` directory and optionally merge with an existing `CLAUDE.md`.

---

## Folder Structure

```text
.claude/
├── CLAUDE.md
├── agents/
│   ├── fastapi-architect.md
│   ├── api-implementer.md
│   ├── async-reviewer.md
│   ├── migration-guard.md
│   ├── pr-reviewer.md
│   └── architecture-enforcer.md
├── commands/
│   ├── design-api.md
│   ├── implement-api.md
│   ├── review-async.md
│   ├── check-migration.md
│   ├── review-api.md
│   ├── plan-feature.md
│   └── refactor.md
└── skills/
    ├── fastapi-architecture.md
    ├── sqlalchemy-async.md
    ├── alembic-safety.md
    └── rest-response-standard.md
```

---

## Example App

See [`examples/fastapi-sample-app/`](examples/fastapi-sample-app/) for a full reference implementation with users, projects, subscriptions, and notifications — including a real Alembic migration and a before/after showing exactly what the agents catch.

---

## Docs

- [Getting Started](docs/getting-started.md)
- [Agent Guide](docs/agent-guide.md)
- [Commands Guide](docs/commands-guide.md)
- [Contributing](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)
