# Before / After Walkthrough

This directory shows what the projects router looked like before and after running the claude-fastapi-pack agents.

## The bad version

`bad_projects_router.py` was written quickly — the kind of code that ships when there are no conventions in place. It works at low traffic but breaks under load and has a critical security bug.

## Running the agents against it

```
/review-async before_after/bad_projects_router.py
```

```
/review-api before_after/bad_projects_router.py
```

## What the agents found

| # | Problem | Severity | Where |
|---|---|---|---|
| 1 | Business logic in route handler | High | `list_projects`, `create_project`, `delete_project` |
| 2 | Direct DB access bypasses service/repository | High | All three routes |
| 3 | N+1 query — one SELECT per project to fetch owner | High | `list_projects` loop |
| 4 | `requests.post()` sync call inside async handler | High | `create_project` |
| 5 | Raw dict responses — no response model validation | Medium | All three routes |
| 6 | Missing auth on DELETE — unauthenticated deletes allowed | Critical | `delete_project` |

## The clean version

`clean_projects_router.py` fixes all six issues.

**Routes are now 3–5 lines each.** All logic lives in `service.py`, all queries in `repository.py`.

**N+1 is gone.** `project_repo.list_by_owner()` issues one query. `owner_id` is on the model so no second lookup is needed. If owner `name` is required, one `joinedload()` handles it.

**Async webhook.** `requests.post()` → `httpx.AsyncClient`. The call also moved to after the DB transaction commits — the session is never held open during an external HTTP call.

**Typed responses.** `response_model=ProjectResponse` on every route.

**Auth on delete.** `get_current_user` dependency added. Ownership check happens inside `project_service.archive_project()` — not in the route.

## Diff summary

```
bad_projects_router.py   →   clean_projects_router.py
────────────────────────────────────────────────────
130 lines                →   60 lines
3 raw dict returns       →   0 (all use response_model)
1 sync HTTP call         →   1 async HTTP call (httpx)
1 N+1 loop               →   0 (single repository query)
0 auth on DELETE         →   get_current_user dependency
DB logic in routes       →   all in service + repository
```
