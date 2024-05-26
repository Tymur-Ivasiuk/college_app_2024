from typing import AsyncGenerator
from abc import abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from src.core.config import settings
from .db_utils import intpk, updated_at, created_at, str50


class Base(DeclarativeBase):
    type_annotation_map = {
        intpk: intpk,
        str50: str50,
        updated_at: updated_at,
        created_at: created_at,
    }

    @abstractmethod
    def to_read_model(self):
        raise NotImplemented


async_engine = create_async_engine(
    url=settings.DB_ASYNC_URL,
    echo=False,
)
async_session_maker = async_sessionmaker(
    async_engine,
    expire_on_commit=False
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
