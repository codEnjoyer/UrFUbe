from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse

from auth.base_config import fastapi_users, auth_backend, current_user
from auth.models import User
from auth.schemas import UserRead, UserCreate

# from routers.users_endpoints import router as router_users
from tasks.router import router as router_tasks

from videos.router import router as video_router

app = FastAPI(title='First FastAPI app')

# app.include_router(router_users)

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
    return f"Hello, {user.username}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonymous!"


@app.get("/", response_class=HTMLResponse)
def main_window():
    return '''
    <html>
        <head>
            <title> TEST VIDEO SERVICES </title>
        </head>
        <body>
            <h1> ЗДЕСЬ МОГЛА БЫТЬ ВАША РЕКЛАМА </h1>
            <video width="500" src="https://storage.yandexcloud.net/urfube-love-coding/video.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=YCAJElLaaDPL9n0QVuF7Jzo_v%2F20230514%2Fru-central1%2Fs3%2Faws4_request&X-Amz-Date=20230514T192934Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=6193ef9a81810fc2cb5db85158461c5d86cd8dfcd928f2b9d5bf22f3c84c26e3" controls></video>
        </body>
    </html>
    '''
