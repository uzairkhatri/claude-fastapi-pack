---
description: Review and fix async FastAPI code — applies all fixes directly to the file.
argument-hint: <file path>
---

Use the `async-reviewer` agent mindset.

Task:
Review the provided async FastAPI code for async safety issues, then apply all fixes directly to the file.

Input:
$ARGUMENTS

Instructions:
- Identify all async issues: blocking calls, session misuse, missing auth, N+1 queries, raw dict returns, business logic in routes
- Apply every fix directly to the file — do not just report
- Replace sync HTTP calls (requests) with async equivalents (httpx.AsyncClient)
- Move business logic out of routes into a service layer
- Move DB queries out of routes into a repository layer
- Add missing auth dependencies
- Replace raw dict returns with typed response models
- Preserve the original file structure and naming, only fix what is broken
- After applying fixes, output a summary table of what was changed and why

Return output in this format:

## Fixes Applied

| # | Problem | Fix |
|---|---|---|

## What Changed
Brief explanation of each fix.

## Next Steps
Any follow-up work needed (e.g. creating the service/repository files referenced).
