from fastapi import FastAPI, Depends

from auth.base_config import fastapi_users, auth_backend, current_user
from auth.models import User
from auth.schemas import UserRead, UserCreate

from tasks.router import router as router_tasks
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


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(router_tasks)
app.include_router(video_router)


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}, your id in database: {user.id}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonymous!"
