from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.notifications.models import Notification


async def list_for_user(
    db: AsyncSession, user_id: int, limit: int, offset: int, unread_only: bool = False
) -> list[Notification]:
    query = select(Notification).where(Notification.user_id == user_id)
    if unread_only:
        query = query.where(Notification.is_read == False)  # noqa: E712
    query = query.order_by(Notification.created_at.desc()).limit(limit).offset(offset)
    result = await db.execute(query)
    return list(result.scalars().all())


async def create(db: AsyncSession, user_id: int, title: str, body: str) -> Notification:
    notif = Notification(user_id=user_id, title=title, body=body)
    db.add(notif)
    await db.flush()
    return notif


async def mark_read(db: AsyncSession, notification: Notification) -> Notification:
    notification.is_read = True
    await db.flush()
    return notification


async def get_by_id_and_user(db: AsyncSession, notif_id: int, user_id: int) -> Notification | None:
    result = await db.execute(
        select(Notification).where(
            Notification.id == notif_id, Notification.user_id == user_id
        )
    )
    return result.scalar_one_or_none()
