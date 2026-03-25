from datetime import datetime

from pydantic import BaseModel

from app.subscriptions.models import Plan, SubscriptionStatus


class SubscriptionResponse(BaseModel):
    id: int
    user_id: int
    plan: Plan
    status: SubscriptionStatus
    started_at: datetime
    expires_at: datetime | None

    model_config = {"from_attributes": True}


class SubscriptionUpgrade(BaseModel):
    plan: Plan
