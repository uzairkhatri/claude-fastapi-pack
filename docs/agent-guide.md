# Agent Guide

Agents are specialized subprocesses that Claude Code can spawn to handle focused tasks. This pack includes six agents.

## fastapi-architect

**When to use:** Starting a new API feature or reviewing whether an existing module structure is clean.

**What it does:** Translates feature requirements into a production-ready backend structure — file layout, route/service/schema/data layer responsibilities, edge cases, and a step-by-step implementation plan.

**Invoked by:** `/design-api`, `/plan-feature`

---

## api-implementer

**When to use:** You have a requirement and need an implementation-ready plan with explicit endpoint contracts and service flow.

**What it does:** Defines endpoints, request/response schemas, service flow, data operations, error cases, and a step-by-step task list a developer can build from directly.

**Invoked by:** `/implement-api`, `/plan-feature`

---

## async-reviewer

**When to use:** Before merging any async code — services, routers, background tasks.

**What it does:** Scans for blocking calls in async context, DB session misuse, external calls inside transaction scope, missing awaits, concurrency risks, and N+1 queries.

**Invoked by:** `/review-async`

---

## migration-guard

**When to use:** Before every Alembic migration merge to production.

**What it does:** Reviews schema changes for destructive operations, nullable/default/backfill issues, rollback risks, lock impact on large tables, and unsafe rollout sequencing. Returns Risk Level + Safer Rollout Plan.

**Invoked by:** `/check-migration`

---

## pr-reviewer

**When to use:** Reviewing a PR before merge.

**What it does:** Full review covering correctness, broken assumptions, architecture alignment, DB/session safety, validation gaps, and maintainability. Produces specific must-fix issues and next actions for the author.

**Invoked by:** `/review-api`

---

## architecture-enforcer

**When to use:** You have a working but messy file — logic mixed into routes, DB queries in handlers, sync calls in async functions — and need it refactored into clean architecture.

**What it does:** Maps every function and block to the layer it belongs in (route / service / repository / schema), produces complete refactored files for each layer, fixes async issues inline, and summarises every change made.

**Invoked by:** `/refactor`
