from datetime import datetime

from sqlalchemy import Boolean, DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)

    projects: Mapped[list["Project"]] = relationship("Project", back_populates="owner", lazy="noload")  # noqa: F821
    notifications: Mapped[list["Notification"]] = relationship("Notification", back_populates="user", lazy="noload")  # noqa: F821
    subscription: Mapped["Subscription"] = relationship("Subscription", back_populates="user", uselist=False, lazy="noload")  # noqa: F821
