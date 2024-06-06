import contextlib

from fastapi import HTTPException
from fastapi_users.exceptions import UserAlreadyExists

from db import get_async_session
from schemas.users.base_user import BaseUserCreateDTO
from utils import get_user_db, get_user_manager


class BaseUserServiceMixin:
    @staticmethod
    async def _create_user(user_data: dict):
        get_async_session_context = contextlib.asynccontextmanager(get_async_session)
        get_user_db_context = contextlib.asynccontextmanager(get_user_db)
        get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)

        try:
            async with get_async_session_context() as session:
                async with get_user_db_context(session) as user_db:
                    async with get_user_manager_context(user_db) as user_manager:
                        user_create_data = BaseUserCreateDTO(**user_data)
                        user = await user_manager.create(user_create_data)
                        return user.id
        except UserAlreadyExists:
            raise HTTPException(status_code=409, detail="User already exists")
