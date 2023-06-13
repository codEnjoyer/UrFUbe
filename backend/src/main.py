from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from auth.router import router as auth_router
from database import get_async_session

from tasks.router import router as tasks_router
from videos.router import router as video_router
from utils.router import router as utils_router

from fastapi.middleware.cors import CORSMiddleware
from config import FRONT_APP_PORT

app = FastAPI(title='First FastAPI app')

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
    f"http://localhost:{FRONT_APP_PORT}",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(tasks_router)
app.include_router(video_router)
app.include_router(utils_router)


# TODO: Написать fetch видосов
@app.get("/",
         description="Первые 15 видео с самым лучшим рейтингом на хостинге",
         status_code=status.HTTP_200_OK,
         tags=["Video"])
async def root(offset: int = 0, limit: int = 15, session: AsyncSession = Depends(get_async_session)):
    # query = select(Video).order_by(Video.count_likes).offset(offset).limit(limit)
    # result = await session.execute(query)
    # videos = result.scalars().all()
    # return videos
    return []
