from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
# from fastapi.middleware.cors import CORSMiddleware

from auth.base_config import fastapi_users, auth_backend, current_user
from auth.models import User
from auth.schemas import UserRead, UserCreate

from tasks.router import router as router_tasks
from auth.manager import get_user_by_id
from videos.router import router as video_router, get_presigned_url, get_user_video_models

from config import FRONT_APP_PORT

app = FastAPI(title='First FastAPI app')

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[f"http://localhost:{FRONT_APP_PORT}"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

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


@app.get("/", response_class=HTMLResponse)
async def main_window():
    #video = await get_user_video_models(1, 1)
    #url = await get_presigned_url(f"{video.video_url}")
    return f'''
    <html>
        <head>
            <title> TEST VIDEO SERVICES </title>
        </head>
        <body>
            <h1> ЗДЕСЬ МОГЛА БЫТЬ ВАША РЕКЛАМА </h1>
            <video width="500" src="url" controls></video>
        </body>
    </html>
    '''
