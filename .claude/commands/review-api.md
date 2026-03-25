# /review-api

Review FastAPI routes and schemas for correctness, security, and API contract quality.

## Agents used
- **pr-reviewer** — correctness, security, HTTP semantics, test coverage

## Usage

```
/review-api [file or directory path]
```

---

## Output format

Respond in exactly this structure. No deviations.

```
## Summary
X comment(s) — Y must-fix, Z suggestions.
Files reviewed: path/to/router.py, path/to/schemas.py

## Must Fix
Issues that must be resolved before this code is safe to merge.

ISSUE 1
  File:     path/to/router.py:LINE
  Category: [Security | Correctness | Missing auth | Unhandled error | Bad status code]
  Problem:  What is wrong and what could go wrong in production.
  Fix:
    # corrected code snippet or description of change needed

ISSUE 2
  ...

(none — if no must-fix issues found)

## Suggestions
Improvements that are not blockers but will reduce future incidents or confusion.

SUGGESTION 1
  File:     path/to/router.py:LINE
  Category: [Naming | Response model | Validation | Pagination | Consistency]
  Note:     What to improve and why.

SUGGESTION 2
  ...

(none — if no suggestions)

## API Contract
Routes reviewed and their contract assessment.

METHOD  /path               Status code   Auth    Response model    Assessment
------  ------------------  ------------  ------  ----------------  ----------
POST    /resource           201           ✓       ✓                 OK
GET     /resource           200           ✓       ✓                 OK
DELETE  /resource/{id}      204           ✗       —                 FAIL — missing auth

## Verdict
APPROVE          — no issues, ready to merge
REQUEST CHANGES  — one or more must-fix issues
COMMENT          — suggestions only, author's call
```
