# Examples

## Designing a new resource

```
/design-api order management with line items and status history
```

The `fastapi-architect` agent will return a proposed file layout:

```
routers/orders.py
services/order_service.py
repositories/order_repo.py
schemas/order.py
models/order.py
models/order_line_item.py
models/order_status_event.py
```

...with rationale for each file and dependency injection wiring.

---

## Planning a full feature

```
/plan-feature email verification flow for user registration
```

Returns:
1. Architecture design with file list
2. Schema definitions for request/response
3. Service and repository function signatures
4. Alembic migration needed
5. Test checklist

---

## Reviewing for async safety

```
/review-async services/notification_service.py
```

Returns flagged issues such as:

```
services/notification_service.py:47
Category: Blocking I/O in async handler
Issue: requests.post() is a sync call inside async send_email()
Fix: Use httpx.AsyncClient instead
```

---

## Checking a migration

```
/check-migration alembic/versions/20260324_drop_legacy_tokens.py
```

Returns:

```
FAIL
[CRITICAL] DROP TABLE legacy_tokens — no downgrade() implemented
[WARNING]  Table has ~2M rows — consider scheduling off-peak
```

## Reference app

See [`examples/fastapi-sample-app/`](../examples/fastapi-sample-app/) for a complete FastAPI app built using this pack's conventions.
