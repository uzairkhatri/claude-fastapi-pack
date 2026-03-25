# Skill: Alembic Migration Safety

## Purpose
Provide reusable guidance for reviewing and planning production-safe schema migrations.

## Principles
- avoid destructive changes unless necessary
- separate schema change from data migration when possible
- preserve backward compatibility during rollout
- consider rollback before shipping
- minimize lock risk on large tables

## Common Safe Rollout Pattern
1. add nullable column or additive schema
2. deploy code that can work with both old and new shapes
3. backfill data
4. add constraints if needed
5. remove old column in later migration

## High-Risk Changes
- drop column/table
- rename column without compatibility strategy
- add non-null column without default/backfill
- change type without data validation
- foreign key changes on hot tables
- index operations without considering traffic/load

## Review Questions
- can old app code still run after this migration?
- can new app code run before full backfill?
- what breaks if rollback happens mid-way?
- is this migration safe on large existing data?
- is there a safer two-step or three-step version?

## Preferred Review Output
Always state:
- risk level
- what is risky
- why it is risky
- safer alternative
- rollout order
