from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from fastapi_users import FastAPIUsers
from starlette.responses import JSONResponse
from pydantic import BaseModel

from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate
from routers.users_endpoints import router

app = FastAPI(title='First FastAPI app')


app.include_router(router)


@app.get("/hello", response_class=PlainTextResponse)
async def get_log():
    return "hello\nworld\n!"


@app.get("/")
async def homepage():
    return JSONResponse({'hello': 'world'})


@app.get('/echo', response_class=PlainTextResponse)
def d(request: Request):
    v = request.headers.items()
    return '\n'.join(f'{i[0]}: {i[1]}' for i in v)


class Item(BaseModel):
    text: str


@app.post("/echo")
def root(data: Item):
    return {"message": f"You wrote: '{data.text}'"}

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)