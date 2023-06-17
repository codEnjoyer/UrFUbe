from typing import Annotated

from fastapi import APIRouter, Depends

from auth.base_config import current_user
from auth.models import User

router = APIRouter(tags=["Utils"])


@router.get("/protected")
def protected_route(user: Annotated[User, Depends(current_user)]):
    return f"Hello, {user.username}, your id in database: {user.id}"


@router.get("/unprotected")
def unprotected_route():
    return f"Hello, anonymous!"


@router.get("/health")
def health():
    return {"status": "OK"}
