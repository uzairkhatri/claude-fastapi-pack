# /refactor

Paste a messy FastAPI file. Get back clean, production-ready code split across the correct layers.

## Agent used
- **architecture-enforcer** — maps code to layers, refactors into router / service / repository / schemas, fixes async issues

## Usage

```
/refactor <file path or pasted code>
```

## What this does

1. **Maps** every function and block in your file to the layer it actually belongs in
2. **Refactors** the code into separate, correctly structured files
3. **Fixes** async issues found during the refactor (blocking calls, N+1s, missing awaits)
4. **Summarises** what changed and what still needs attention

---

## Output format

Respond in exactly this structure. No deviations.

```
## Layer Map
Table showing every piece of code, where it lives now, where it should live, and why.

| Code | Current location | Correct layer | Reason |
|---|---|---|---|
| ... | ... | ... | ... |

## Refactored Files

### app/<domain>/router.py
```python
# complete file
```

### app/<domain>/service.py
```python
# complete file
```

### app/<domain>/repository.py
```python
# complete file
```

### app/<domain>/schemas.py
```python
# complete file
```

### app/<domain>/models.py
```python
# only if model changes needed
```

## Changes Summary

Before:  X lines in 1 file
After:   Y lines across N files

Issues resolved:
- [x] Moved ownership check from route to service
- [x] Replaced requests.post() with httpx.AsyncClient
- [x] Eliminated N+1 query in list handler
- [x] Added response_model to all routes
- [x] Added auth dependency to delete route

Async issues fixed:
- [x] ...  (or "none found")

Remaining risks:
- Item (or "none")
```

---

## Example

Input:
```
/refactor app/orders.py
```

Output: a full layer map, then `router.py`, `service.py`, `repository.py`, `schemas.py` — each as a complete, working file — followed by a summary of every structural and async issue that was corrected.
