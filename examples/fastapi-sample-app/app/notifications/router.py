from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.dependencies.auth import get_current_user
from app.notifications import service as notif_service
from app.notifications.schemas import NotificationResponse
from app.users.models import User

router = APIRouter()


@router.get("/", response_model=list[NotificationResponse])
async def list_notifications(
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    unread_only: bool = Query(False),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await notif_service.list_notifications(db, current_user, limit, offset, unread_only)


@router.post("/{notif_id}/read", response_model=NotificationResponse)
async def mark_as_read(
    notif_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await notif_service.mark_as_read(db, notif_id, current_user)
