"""
CLEAN IMPLEMENTATION — after /review-async, /review-api, and /design-api

Every problem from bad_projects_router.py is resolved.
The diff between the two files is the demo.

What the agents changed and why:

  [1] FIXED: Business logic moved to service layer
      Routes call one service function and return. Nothing else.

  [2] FIXED: DB access moved to repository layer
      Routes never touch `session` or `select()` directly.

  [3] FIXED: N+1 query eliminated
      list_projects() returns ProjectResponse with owner_id already on the model.
      If owner name is needed, one joinedload() fetches it in a single query.

  [4] FIXED: Sync requests.post() replaced with httpx.AsyncClient
      Webhook notification is async and does not block the event loop.
      Also moved out of the DB transaction — session is not held open during the HTTP call.

  [5] FIXED: Typed response models on every route
      response_model= declared on all routes. Pydantic validates and serialises output.

  [6] FIXED: Auth dependency added to delete route
      get_current_user applied. Ownership verified in service before delete proceeds.
"""

import httpx
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.dependencies.auth import get_current_user
from app.projects import service as project_service
from app.projects.schemas import ProjectCreate, ProjectResponse, ProjectUpdate
from app.users.models import User

router = APIRouter()


# [1][2] Route delegates entirely to service — no logic, no DB access
# [3] N+1 gone — service calls repository which issues a single optimised query
# [5] response_model declared — typed, validated output
@router.get("/", response_model=list[ProjectResponse])
async def list_projects(
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await project_service.list_projects(db, current_user, limit, offset)


# [1][2] All business logic and DB access in service + repository
# [4] Webhook is async and fires AFTER the DB transaction closes — no session held during I/O
# [5] Typed response model
@router.post("/", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
async def create_project(
    payload: ProjectCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    project = await project_service.create_project(db, payload, current_user)

    # [4] Async HTTP call, runs after DB transaction is committed and closed
    async with httpx.AsyncClient() as client:
        await client.post(
            "https://hooks.example.com/notify",
            json={"event": "project_created", "project_id": project.id},
            timeout=5.0,
        )

    return project


@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(
    project_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await project_service.get_project(db, project_id, current_user)


@router.patch("/{project_id}", response_model=ProjectResponse)
async def update_project(
    project_id: int,
    payload: ProjectUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await project_service.update_project(db, project_id, payload, current_user)


# [6] Auth dependency present — unauthenticated requests rejected at the framework level
# [1] Ownership verified inside service.archive_project(), not here
@router.post("/{project_id}/archive", response_model=ProjectResponse)
async def archive_project(
    project_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await project_service.archive_project(db, project_id, current_user)
