# Skill: SQLAlchemy Async Safety

## Purpose
Provide reusable async and AsyncSession guidance for FastAPI applications.

## Principles
- keep transactions short
- do not hold DB session open during slow external work
- avoid network/API/LLM calls inside transaction scope
- understand flush vs commit
- prefer explicit transaction intent

## Review Rules
Check for:
- blocking sync code in async functions
- long DB session lifetime
- external calls before commit while transaction is open
- missing await on async DB operations
- inconsistent transaction flow
- session reuse across unrelated operations

## Good Patterns
- fetch DB data
- exit transaction-sensitive section quickly
- perform slow external work outside transaction
- reopen transaction only when needed
- use flush() when the ID is needed before commit()

## Dangerous Patterns
- API/LLM calls inside `async with db.begin():`
- large loops doing DB + network together
- mixed sync and async DB utilities
- commit scattered across many layers
- hidden DB writes inside helper functions

## Guidance
Prefer patterns that make it obvious:
- when a transaction starts
- when DB writes happen
- when external dependencies are called
- where retries/timeouts should live
