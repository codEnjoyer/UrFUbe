from typing import Optional

import boto3
from botocore.exceptions import ClientError
from fastapi import Depends, Request, HTTPException
from fastapi_users import BaseUserManager, IntegerIDMixin, schemas, models, exceptions, InvalidPasswordException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from auth.schemas import UserCreate, UserRead

from auth.models import User, get_user_db

from config import RESET_PASSWORD_TOKEN, VERIFICATION_TOKEN, BUCKET_NAME
from utils.mail import send_welcome_email

session = boto3.session.Session()
s3 = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net'
)


def create_user_folder(user_id: int):
    try:
        s3.put_object(Bucket=BUCKET_NAME, Key=f"{user_id}/")
    except ClientError as e:
        print(f"User {user_id} has not registered")
        return None
    print(f"User {user_id} has registered.")


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = RESET_PASSWORD_TOKEN
    verification_token_secret = VERIFICATION_TOKEN

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        create_user_folder(user.id)
        send_welcome_email(user)

    async def create(
            self,
            user_create: schemas.UC,
            safe: bool = False,
            request: Optional[Request] = None,
    ) -> models.UP:
        await self.validate_password(user_create.password, user_create)

        existing_user = await self.user_db.get_by_email(user_create.email)
        if existing_user is not None:
            raise exceptions.UserAlreadyExists()

        user_dict = (
            user_create.create_update_dict()
            if safe
            else user_create.create_update_dict_superuser()
        )
        password = user_dict.pop("password")
        user_dict["hashed_password"] = self.password_helper.hash(password)
        created_user = await self.user_db.create(user_dict)
        await self.on_after_register(created_user, request)
        return created_user

    async def validate_password(
            self,
            password: str,
            user: UserCreate | User,
    ) -> None:
        should_password_len = 8
        if len(password) < should_password_len:
            raise InvalidPasswordException(
                reason=f"Password should be at least {should_password_len} characters"
            )
        if user.email in password:
            raise InvalidPasswordException(
                reason="Password should not contain e-mail"
            )


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)


async def get_user_by_id(async_session: AsyncSession, user_id: int) -> UserRead:
    try:
        stmt = select(User).filter(User.id == user_id)
        user = await async_session.scalar(stmt)
        if user is None:
            raise HTTPException(status_code=400, detail="Invalid user_id")
        return UserRead(id=user.id,
                        email=user.email,
                        username=user.username)
    except Exception as e:
        await async_session.rollback()
        raise e
    finally:
        await async_session.close()
