from typing import Optional

import boto3
from botocore.exceptions import ClientError
from fastapi import Depends, Request, HTTPException
from fastapi_users import BaseUserManager, IntegerIDMixin, schemas, models, exceptions
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import engine

from auth.models import User, get_user_db

from config import SECRET_AUTH, BUCKET_NAME

session = boto3.session.Session()
s3 = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net'
)


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET_AUTH
    verification_token_secret = SECRET_AUTH

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        try:
            s3.put_object(Bucket=BUCKET_NAME, Key=f"{user.username}/")
        except ClientError as e:
            print(f"User {user.id} has not registered")
            return None
        print(f"User {user.id} has registered.")

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
        # user_dict["id"] = 12
        user_dict["hashed_password"] = self.password_helper.hash(password)

        created_user = await self.user_db.create(user_dict)

        await self.on_after_register(created_user, request)

        return created_user


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)


async def get_user_by_id(user_id: int):
    async with engine.begin() as connection:
        async_session = AsyncSession(bind=connection)
        try:
            stmt = select(User).filter(User.id == user_id)
            user = await async_session.scalar(stmt)
            if user is None:
                raise HTTPException(status_code=400, detail="Invalid user_id")
            return user
        except Exception as e:
            await async_session.rollback()
            raise e
        finally:
            await async_session.close()
