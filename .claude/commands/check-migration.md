---
description: Review a migration plan or Alembic migration for safety, rollback concerns, and production-readiness.
argument-hint: <migration code or schema change summary>
---

Use the `migration-guard` agent mindset.

Task:
Review the migration for production risk and rollout safety.

Input:
$ARGUMENTS

Instructions:
- Evaluate schema safety
- Flag destructive operations
- Check nullability/default/backfill issues
- Assess rollback concerns
- Suggest safer rollout sequence
- Be practical and production-focused

Return output in this format:

## Migration Summary
## Risk Level
## Critical Risks
## Data Safety Concerns
## Rollback Concerns
## Safer Rollout Plan
## Recommended Migration Changes
