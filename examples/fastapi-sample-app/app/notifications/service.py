from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.notifications import repository as notif_repo
from app.notifications.models import Notification
from app.users.models import User


async def list_notifications(
    db: AsyncSession,
    user: User,
    limit: int = 20,
    offset: int = 0,
    unread_only: bool = False,
) -> list[Notification]:
    return await notif_repo.list_for_user(db, user.id, limit, offset, unread_only)


async def mark_as_read(db: AsyncSession, notif_id: int, user: User) -> Notification:
    notif = await notif_repo.get_by_id_and_user(db, notif_id, user.id)
    if not notif:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Notification not found")
    if notif.is_read:
        return notif

    async with db.begin():
        return await notif_repo.mark_read(db, notif)
