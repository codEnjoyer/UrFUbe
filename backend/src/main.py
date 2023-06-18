from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from auth.router import router as auth_router
from database import get_async_session

from users.router import router as user_router
from videos.router import router as video_router, get_last_video_models
from utils.router import router as utils_router

from fastapi.middleware.cors import CORSMiddleware
from config import FRONT_HOST_PORT, FRONT_APP_PORT

app = FastAPI(title='First FastAPI app')

origins = [
    "http://localhost",
    f"http://localhost:{FRONT_APP_PORT}",
    f"http://localhost:{FRONT_HOST_PORT}",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(video_router)
app.include_router(utils_router)


@app.get("/",
         description="Первые 15 видео с самым лучшим рейтингом на хостинге",
         status_code=status.HTTP_200_OK,
         tags=["Video"])
async def root(offset: int = 0, limit: int = 15, async_session: AsyncSession = Depends(get_async_session)):
    return await get_last_video_models(async_session, offset, limit)
