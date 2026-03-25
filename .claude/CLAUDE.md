# Claude FastAPI Pack - Project Standards

You are working in a production-oriented FastAPI codebase.

## Primary Goal
Help developers design, implement, and review FastAPI systems using clear architecture, safe async patterns, and maintainable code structure.

## Core Principles
- Prefer clean, production-friendly architecture over shortcuts
- Be explicit, structured, and implementation-oriented
- Keep responses practical and directly usable
- Favor maintainability, testability, and scalability
- Do not suggest overly complex abstractions unless justified

## Architecture Rules
- Follow Router -> Service -> Model/Repository separation
- Routes should stay thin
- Business logic belongs in services
- Data access belongs in models/repositories
- Schemas should validate and serialize data only
- Avoid mixing route, service, and DB logic in one file

## FastAPI Rules
- Use dependency injection cleanly
- Keep endpoints small and readable
- Validate request and response payloads
- Prefer explicit response models
- Keep naming consistent with project modules

## Async + DB Safety Rules
- Avoid long-running external calls inside DB session blocks
- Avoid API/LLM/network calls while holding a transaction open
- Use AsyncSession patterns correctly
- Prefer flush() when IDs are needed before commit
- Do not recommend blocking operations inside async flows

## Migration Rules
- Flag risky schema changes clearly
- Identify destructive operations
- Consider rollback implications
- Suggest safer migration paths when possible
- Watch for nullable/default/backfill issues

## Review Priorities
In order of importance:
1. correctness
2. architecture
3. safety
4. maintainability
5. performance
6. readability

## Output Style
- Be structured
- Use headings
- Give exact recommendations
- Prefer actionable next steps
- Avoid vague feedback like "looks good"
