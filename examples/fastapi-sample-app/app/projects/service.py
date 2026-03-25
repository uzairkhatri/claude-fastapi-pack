from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.projects import repository as project_repo
from app.projects.models import Project
from app.projects.schemas import ProjectCreate, ProjectUpdate
from app.users.models import User


async def create_project(db: AsyncSession, payload: ProjectCreate, owner: User) -> Project:
    async with db.begin():
        return await project_repo.create(db, owner.id, payload.name, payload.description)


async def list_projects(
    db: AsyncSession, owner: User, limit: int = 20, offset: int = 0
) -> list[Project]:
    return await project_repo.list_by_owner(db, owner.id, limit, offset)


async def get_project(db: AsyncSession, project_id: int, owner: User) -> Project:
    project = await project_repo.get_by_id_and_owner(db, project_id, owner.id)
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return project


async def update_project(
    db: AsyncSession, project_id: int, payload: ProjectUpdate, owner: User
) -> Project:
    project = await project_repo.get_by_id_and_owner(db, project_id, owner.id)
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    async with db.begin():
        return await project_repo.update(db, project, payload.name, payload.description)


async def archive_project(db: AsyncSession, project_id: int, owner: User) -> Project:
    project = await project_repo.get_by_id_and_owner(db, project_id, owner.id)
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    if project.is_archived:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Project already archived")

    async with db.begin():
        return await project_repo.archive(db, project)
