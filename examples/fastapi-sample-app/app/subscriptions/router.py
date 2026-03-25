from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.dependencies.auth import get_current_user
from app.subscriptions import service as sub_service
from app.subscriptions.schemas import SubscriptionResponse, SubscriptionUpgrade
from app.users.models import User

router = APIRouter()


@router.get("/", response_model=SubscriptionResponse)
async def get_subscription(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await sub_service.get_or_create(db, current_user)


@router.post("/upgrade", response_model=SubscriptionResponse)
async def upgrade_subscription(
    payload: SubscriptionUpgrade,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await sub_service.upgrade(db, current_user, payload.plan)


@router.post("/cancel", response_model=SubscriptionResponse)
async def cancel_subscription(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await sub_service.cancel(db, current_user)
