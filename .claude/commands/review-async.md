---
description: Review async FastAPI or Async SQLAlchemy code for blocking operations, session misuse, and concurrency risks.
argument-hint: <code snippet, file, or implementation summary>
---

Use the `async-reviewer` agent mindset.

Task:
Review the provided async FastAPI / Async SQLAlchemy code for correctness, async safety, and scalability risks.

Input:
$ARGUMENTS

Instructions:
- Identify critical async issues first
- Check for blocking calls
- Check DB session lifetime and transaction issues
- Check for external calls inside DB session scope
- Check concurrency and maintainability risks
- Suggest safer patterns

Return output in this format:

## Review Summary
## Critical Issues
## Medium Issues
## DB Session Risks
## Concurrency Risks
## Recommended Fixes
## Safer Pattern
