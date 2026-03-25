# Commands Guide

Slash commands are shortcuts that invoke one or more agents with context from your project.

## /design-api

Design the full structure for a new API feature — routes, services, schemas, data layer, edge cases, and implementation plan.

```
/design-api <feature description>
```

**Example:**
```
/design-api product catalog with category filtering and pagination
```

---

## /implement-api

Turn a feature requirement into an implementation-ready plan with explicit endpoint contracts, service flow, and a step-by-step task list.

```
/implement-api <feature requirement>
```

**Example:**
```
/implement-api user invite flow with email verification
```

---

## /review-async

Audit code for async correctness and scalability risks — blocking calls, DB session misuse, external calls inside transactions, missing awaits, N+1 queries.

```
/review-async <code snippet, file, or implementation summary>
```

**Example:**
```
/review-async app/services/order_service.py
```

---

## /check-migration

Safety-check an Alembic migration or schema change plan before it goes to production.

```
/check-migration <migration code or schema change summary>
```

**Example:**
```
/check-migration alembic/versions/20260324_add_orders_table.py
```

---

## /review-api

Review FastAPI routes and schemas for correctness, architecture alignment, validation gaps, and production readiness.

```
/review-api <code snippet or file>
```

**Example:**
```
/review-api app/routers/orders.py
```

---

## /plan-feature

Generate a complete implementation plan before writing any code — architecture decisions, file list, implementation checklist, test checklist, and risks.

```
/plan-feature <feature description>
```

**Example:**
```
/plan-feature Stripe webhook handler for subscription lifecycle events
```

---

## /refactor

Paste a messy FastAPI file. Get back clean architecture split across the correct layers with async issues fixed.

```
/refactor <file path or pasted code>
```

**Example:**
```
/refactor app/orders.py
```

Produces a layer map showing where each piece of code currently lives and where it should live, complete refactored files for router / service / repository / schemas, and a summary of every issue resolved.
