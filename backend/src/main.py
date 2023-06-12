from fastapi import FastAPI

from auth.router import router as auth_router

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
