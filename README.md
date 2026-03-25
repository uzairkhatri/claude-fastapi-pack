# Claude FastAPI Pack

> Stop using Claude like ChatGPT. Use it like a backend architect.

🚀 Turn Claude into a production-ready FastAPI backend architect

Design APIs, review async code, catch migration risks, and enforce clean architecture — in seconds.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Claude](https://img.shields.io/badge/Claude-Code-purple)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green)
[![GitHub Stars](https://img.shields.io/github/stars/uzairkhatri/claude-fastapi-pack?style=social)](https://github.com/uzairkhatri/claude-fastapi-pack)
![GitHub stars](https://img.shields.io/github/stars/uzairkhatri/claude-fastapi-pack)
![License](https://img.shields.io/badge/license-MIT-green)
![FastAPI](https://img.shields.io/badge/FastAPI-ready-blue)

---

## 🚨 Why This Is Different

Most Claude repos:
- share prompts
- explain concepts
- give generic workflows

This repo:
- gives plug-and-play agents
- enforces real backend architecture
- focuses on production FastAPI systems

---

## ⚡ What This Solves

Most FastAPI projects suffer from:

❌ Fat route handlers
❌ Mixed business logic + DB queries
❌ Async bugs and session misuse
❌ Risky migrations shipped blindly
❌ Inconsistent architecture across teams

---

## ✅ What You Get

With this pack, Claude becomes your:

- 🧠 Backend Architect
- 🔍 Async Code Reviewer
- 🛡️ Migration Safety Guard
- ⚙️ API Designer
- 👨‍💻 PR Reviewer

---

## 🎥 Demo

![Demo](assets/screenshots/demo.gif)

---

## 🔥 Before vs After

### ❌ Before (`examples/fastapi-sample-app/before_after/bad_projects_router.py`)

```python
import requests  # sync HTTP inside async handler

@router.post("/")
async def create_project(
    name: str,
    description: str = None,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if len(name) < 3:                          # [1] business logic in route
        raise HTTPException(400, "Name too short")

    project = Project(name=name, owner_id=current_user.id)
    db.add(project)                            # [2] direct DB write — no repository
    await db.commit()
    await db.refresh(project)

    requests.post(                             # [4] sync call blocks the event loop
        "https://hooks.example.com/notify",
        json={"event": "project_created", "project_id": project.id},
    )

    return {"id": project.id, "name": project.name}  # [5] raw dict — no response model


@router.delete("/{project_id}")               # [6] no auth — anyone can delete
async def delete_project(project_id: int, db: AsyncSession = Depends(get_db)):
    ...
```

### ✅ After

```python
@router.post("/", response_model=ProjectResponse)
async def create_project(
    payload: ProjectCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await project_service.create(db, payload, owner=current_user)


@router.delete("/{project_id}", status_code=204)
async def delete_project(
    project_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),  # auth restored
):
    await project_service.delete(db, project_id, requestor=current_user)
```

One command found all of this:

```
/review-async examples/fastapi-sample-app/before_after/bad_projects_router.py
```

| # | Problem | Severity |
|---|---|---|
| 1 | Business logic inside route handler | High |
| 2 | Direct DB access — no service or repository layer | High |
| 3 | N+1 query — one SELECT per project to fetch owner | High |
| 4 | `requests.post()` sync call inside async handler | High |
| 5 | Raw dict responses — no response model validation | Medium |
| 6 | Missing auth on DELETE — unauthenticated deletes allowed | **Critical** |

See the [full walkthrough](examples/fastapi-sample-app/before_after/WALKTHROUGH.md).

---

## ⚡ Features

### Agents
- `fastapi-architect` — design features into clean file/module structure
- `api-implementer` — turn requirements into implementation-ready tasks
- `async-reviewer` — catch blocking calls, session misuse, concurrency bugs
- `migration-guard` — flag destructive changes before they hit production
- `pr-reviewer` — full architecture + safety review on every PR
- `architecture-enforcer` — enforce Router → Service → Repository separation

### Commands
- `/design-api` — design a new API feature end to end
- `/implement-api` — scaffold implementation steps
- `/review-async` — review async code for safety issues
- `/check-migration` — validate Alembic migrations before deploy
- `/review-api` — full API review against architecture rules
- `/plan-feature` — plan a feature from requirements
- `/refactor` — refactor toward clean architecture

### Skills
Reusable knowledge loaded automatically:
- FastAPI architecture patterns
- SQLAlchemy async safety rules
- Alembic migration safety checks
- REST response standards

---

## 👤 Built For

- FastAPI developers
- Backend engineers
- SaaS teams
- AI product builders

---

## 🎯 Use Cases

- Design new FastAPI features
- Refactor messy routes into clean architecture
- Review async SQLAlchemy code
- Catch migration risks before deploy
- Improve PR quality across team

---

## 🧠 How It Works

Clean separation enforced by every agent and command:

- Route → Service → Repository
- Safer async patterns
- Structured responses

> Use Claude like a production backend teammate.

---

## ⚙️ Setup in 30 Seconds

```bash
git clone https://github.com/uzairkhatri/claude-fastapi-pack
cp -r .claude your-project/
```

Then inside Claude Code:

```
/design-api Build notification API
```

Done.

<details>
<summary>Other install options</summary>

**One-line install**
```bash
curl -sSL https://raw.githubusercontent.com/uzairkhatri/claude-fastapi-pack/main/install/install.sh | bash
```

**Python script**
```bash
python install/install.py
```

Both copy agents, commands, and skills into your project's `.claude/` directory and optionally merge with an existing `CLAUDE.md`.
</details>

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
