from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from auth.models import User
from sqlalchemy import select


async def get_user(db: AsyncSession, user_id: int) -> User:
    stmt = select(User).where(User.id == user_id)
    return await db.scalar(stmt)


async def get_users(db: AsyncSession, offset: int = 0, limit: int = 15) -> List[User]:
    stmt = select(User).offset(offset).limit(limit)
    return await db.scalars(stmt)
