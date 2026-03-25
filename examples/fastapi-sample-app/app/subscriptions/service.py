from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.subscriptions import repository as sub_repo
from app.subscriptions.models import Plan, Subscription, SubscriptionStatus
from app.users.models import User


async def get_or_create(db: AsyncSession, user: User) -> Subscription:
    sub = await sub_repo.get_by_user_id(db, user.id)
    if not sub:
        async with db.begin():
            sub = await sub_repo.create(db, user.id, Plan.free)
    return sub


async def upgrade(db: AsyncSession, user: User, plan: Plan) -> Subscription:
    sub = await sub_repo.get_by_user_id(db, user.id)
    if not sub:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No subscription found")
    if sub.status == SubscriptionStatus.cancelled:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Subscription is cancelled")
    if sub.plan == plan:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Already on this plan")

    async with db.begin():
        return await sub_repo.update_plan(db, sub, plan)


async def cancel(db: AsyncSession, user: User) -> Subscription:
    sub = await sub_repo.get_by_user_id(db, user.id)
    if not sub:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No subscription found")
    if sub.status == SubscriptionStatus.cancelled:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Already cancelled")

    async with db.begin():
        return await sub_repo.cancel(db, sub)
