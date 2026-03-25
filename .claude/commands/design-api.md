---
description: Design a FastAPI feature into routes, services, schemas, and implementation steps.
argument-hint: <feature requirement or API goal>
---

Use the `fastapi-architect` agent and `api-implementer` agent mindset.

Task:
Design the requested FastAPI feature in a production-ready structure.

User request:
$ARGUMENTS

Instructions:
- Understand the feature requirement
- Propose clean Router -> Service -> Schema -> Data breakdown
- Define endpoints clearly
- Keep route handlers thin
- Include validation, edge cases, and failure paths
- Recommend a practical implementation order
- Be explicit and implementation-ready

Return output in this format:

## Feature Summary
## Recommended Files
## Endpoints
## Request Schemas
## Response Schemas
## Service Responsibilities
## Data Layer Responsibilities
## Edge Cases
## Implementation Plan
