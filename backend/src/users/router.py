from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from starlette import status

from auth.schemas import UserRead
from database import get_async_session
from users.crud import get_user
from videos.router import get_videos_info, get_user_video_models

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id: int,
                         async_session: Annotated[AsyncSession, Depends(get_async_session)],
                         videos_offset: int = 0,
                         videos_limit: int = 15) -> dict:
    videos_models = await get_user_video_models(async_session, user_id, videos_offset, videos_limit)
    videos_read = await get_videos_info(videos_models)
    user = await get_user_info(async_session, user_id)
    return {"videos": videos_read, "user": user}


async def get_user_info(async_session: AsyncSession, user_id: int) -> UserRead:
    db_user = await get_user(async_session, user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user
