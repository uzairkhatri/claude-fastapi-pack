# /plan-feature

Generate a full implementation plan before writing any code.

## Agents used
- **fastapi-architect** — architecture, layers, file breakdown
- **pr-reviewer** — review criteria, test checklist, risk flags

## Usage

```
/plan-feature <feature description>
```

---

## Output format

Respond in exactly this structure. No deviations.

```
## Feature Summary
One paragraph. What this feature does, its inputs and outputs, and the key
business rules it must enforce.

## Architecture Decisions
- Decision one — e.g. "Webhook events stored before processing for auditability"
- Decision two — e.g. "Idempotency key on event.id prevents duplicate processing"
- Decision three — e.g. "Status transitions validated in service, not in DB constraints"

## Recommended Files
New files to create:
- app/<domain>/router.py
- app/<domain>/service.py
- app/<domain>/repository.py
- app/<domain>/schemas.py
- app/<domain>/models.py
- alembic/versions/<timestamp>_<description>.py

Files to modify:
- app/main.py    — register new router

## Implementation Checklist
Complete top to bottom. Each step unblocks the next.

- [ ] Define SQLAlchemy model(s)
- [ ] Write Alembic migration — run /check-migration before merging
- [ ] Define Pydantic request/response schemas
- [ ] Implement repository layer (queries only, no business logic)
- [ ] Implement service layer (business logic, calls repository)
- [ ] Write route handlers (thin — one service call each)
- [ ] Register router in main.py
- [ ] Run /review-async on service file before opening PR

## Test Checklist
Every item must pass before merge.

Happy path:
- [ ] Test description

Edge cases:
- [ ] Test description (e.g. duplicate submission returns 409, not 500)
- [ ] Test description (e.g. expired token returns 401 with correct body)

Error cases:
- [ ] Test description (e.g. DB unavailable returns 503, not an unhandled exception)

## Risks
- Risk one — e.g. "Fanout notifications on large user lists may be slow — consider background task"
- Risk two — e.g. "No rate limiting on this endpoint — consider adding before going public"
```
