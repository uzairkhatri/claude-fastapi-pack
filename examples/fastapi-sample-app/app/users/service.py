from datetime import datetime, timedelta

from fastapi import HTTPException, status
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.users import repository as user_repo
from app.users.models import User
from app.users.schemas import UserCreate

ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def register(db: AsyncSession, payload: UserCreate) -> User:
    existing = await user_repo.get_by_email(db, payload.email)
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")

    hashed = pwd_context.hash(payload.password)
    async with db.begin():
        return await user_repo.create(db, payload.email, hashed, payload.name)


async def login(db: AsyncSession, email: str, password: str) -> str:
    user = await user_repo.get_by_email(db, email)
    if not user or not pwd_context.verify(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )

    expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    token = jwt.encode({"sub": str(user.id), "exp": expire}, settings.secret_key, algorithm=ALGORITHM)
    return token
