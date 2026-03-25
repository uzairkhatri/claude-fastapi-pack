# FastAPI Sample App

A reference implementation built with `claude-fastapi-pack` conventions.

Covers users, projects, subscriptions, and notifications — with a real Alembic migration, a deliberately bad implementation, and the cleaned-up version side by side.

## Stack

- FastAPI + Uvicorn
- SQLAlchemy 2.x async (asyncpg)
- Alembic
- Pydantic v2
- PostgreSQL

## Run locally

```bash
cp .env.example .env
# edit .env with your DB credentials

pip install -r requirements.txt

alembic upgrade head

uvicorn app.main:app --reload
```

API docs at `http://localhost:8000/docs`

## Structure

```
app/
├── main.py
├── config.py
├── database.py
├── dependencies/
├── users/
├── projects/
├── subscriptions/
└── notifications/
```

## Before / After

See [`before_after/`](before_after/) for a side-by-side of:

- `bad_projects_router.py` — logic in routes, N+1 queries, no error handling
- `clean_projects_router.py` — thin routes, service layer, async-safe

## Agents used to build this

```
/design-api project management with owner and member roles
/review-async app/projects/service.py
/check-migration alembic/versions/001_initial_schema.py
/plan-feature notification fanout on project invite
```
