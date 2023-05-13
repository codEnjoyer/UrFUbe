from fastapi import FastAPI, Depends

from auth.base_config import fastapi_users, auth_backend, current_user
from auth.models import User
from auth.schemas import UserRead, UserCreate

# from routers.users_endpoints import router as router_users

app = FastAPI(title='First FastAPI app')

# app.include_router(router_users)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonymous!"

