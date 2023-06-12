from fastapi import FastAPI, Depends

from auth.base_config import current_user
from auth.models import User
from auth.router import router as auth_router

from tasks.router import router as tasks_router
from videos.router import router as video_router
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


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}, your id in database: {user.id}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonymous!"
