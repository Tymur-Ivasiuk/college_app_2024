from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_async_session
from utils.auth_system.manager import UserManager
from models import BaseUser


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, BaseUser)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
