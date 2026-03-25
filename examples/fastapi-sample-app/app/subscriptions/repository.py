from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.subscriptions.models import Plan, Subscription, SubscriptionStatus


async def get_by_user_id(db: AsyncSession, user_id: int) -> Subscription | None:
    result = await db.execute(select(Subscription).where(Subscription.user_id == user_id))
    return result.scalar_one_or_none()


async def create(db: AsyncSession, user_id: int, plan: Plan) -> Subscription:
    sub = Subscription(user_id=user_id, plan=plan, status=SubscriptionStatus.active)
    db.add(sub)
    await db.flush()
    return sub


async def update_plan(db: AsyncSession, subscription: Subscription, plan: Plan) -> Subscription:
    subscription.plan = plan
    await db.flush()
    return subscription


async def cancel(db: AsyncSession, subscription: Subscription) -> Subscription:
    subscription.status = SubscriptionStatus.cancelled
    await db.flush()
    return subscription
