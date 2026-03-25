"""
BAD IMPLEMENTATION — before running /review-async and /review-api

This is what the projects router looked like before the agents reviewed it.
It has 6 distinct problems, all common in real codebases.

Problems flagged by the agents:
  [1] Business logic leaking into the route handler
  [2] Direct DB access in the route — bypasses the service/repository layers
  [3] N+1 query — one SELECT per project to fetch the owner name
  [4] Sync requests.post() call inside an async handler — blocks the event loop
  [5] Raw dict response — skips response model validation entirely
  [6] Missing auth on the DELETE route — any unauthenticated caller can delete projects

Run /review-async and /review-api against this file to see the agents catch all six.
"""

import requests  # [4] sync HTTP library used in async handler
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.dependencies.auth import get_current_user
from app.projects.models import Project
from app.users.models import User

router = APIRouter()


# [1] Business logic in the route — ownership check, archive logic, notification
# [2] Direct DB queries in the route — no service or repository layer
# [3] N+1 — fetches owner for each project in a separate query inside the loop
@router.get("/")
async def list_projects(db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    result = await db.execute(
        select(Project).where(Project.owner_id == current_user.id)
    )
    projects = result.scalars().all()

    output = []
    for project in projects:
        # [3] N+1: one query per project to get owner name
        owner_result = await db.execute(select(User).where(User.id == project.owner_id))
        owner = owner_result.scalar_one()

        output.append({
            "id": project.id,
            "name": project.name,
            "owner": owner.name,  # [5] raw dict, no response model
        })

    return output  # [5] returning a raw list of dicts, not a typed response model


# [1] Ownership check, validation, and notification all crammed into the route
# [4] Sync requests.post() inside an async handler — blocks the event loop for every create
@router.post("/")
async def create_project(
    name: str,
    description: str = None,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # [1] Business logic in route
    if len(name) < 3:
        from fastapi import HTTPException
        raise HTTPException(400, "Name too short")

    # [2] Direct DB write in route — no repository
    project = Project(name=name, description=description, owner_id=current_user.id)
    db.add(project)
    await db.commit()
    await db.refresh(project)

    # [4] Sync HTTP call inside async handler — blocks the event loop
    requests.post(
        "https://hooks.example.com/notify",
        json={"event": "project_created", "project_id": project.id},
    )

    return {"id": project.id, "name": project.name}  # [5] raw dict


# [6] No auth dependency — any unauthenticated request can delete any project
# [1] Ownership check in route instead of service
# [2] Direct DB delete in route
@router.delete("/{project_id}")
async def delete_project(
    project_id: int,
    db: AsyncSession = Depends(get_db),
    # current_user missing — [6] no authentication
):
    result = await db.execute(select(Project).where(Project.id == project_id))
    project = result.scalar_one_or_none()

    # [1] Business rule (ownership) checked in route
    if not project:
        from fastapi import HTTPException
        raise HTTPException(404, "Not found")

    await db.delete(project)
    await db.commit()
    return {"deleted": True}  # [5] raw dict
