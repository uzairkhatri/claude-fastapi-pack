from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.projects.models import Project


async def get_by_id(db: AsyncSession, project_id: int) -> Project | None:
    result = await db.execute(select(Project).where(Project.id == project_id))
    return result.scalar_one_or_none()


async def get_by_id_and_owner(db: AsyncSession, project_id: int, owner_id: int) -> Project | None:
    result = await db.execute(
        select(Project).where(Project.id == project_id, Project.owner_id == owner_id)
    )
    return result.scalar_one_or_none()


async def list_by_owner(db: AsyncSession, owner_id: int, limit: int, offset: int) -> list[Project]:
    result = await db.execute(
        select(Project)
        .where(Project.owner_id == owner_id, Project.is_archived == False)  # noqa: E712
        .order_by(Project.created_at.desc())
        .limit(limit)
        .offset(offset)
    )
    return list(result.scalars().all())


async def create(db: AsyncSession, owner_id: int, name: str, description: str | None) -> Project:
    project = Project(owner_id=owner_id, name=name, description=description)
    db.add(project)
    await db.flush()
    return project


async def update(db: AsyncSession, project: Project, name: str | None, description: str | None) -> Project:
    if name is not None:
        project.name = name
    if description is not None:
        project.description = description
    await db.flush()
    return project


async def archive(db: AsyncSession, project: Project) -> Project:
    project.is_archived = True
    await db.flush()
    return project
