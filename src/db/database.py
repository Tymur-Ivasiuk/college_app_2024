from typing import AsyncGenerator
from abc import abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from src.core.config import settings


class Base(DeclarativeBase):
    @abstractmethod
    def to_read_model(self):
        raise NotImplemented


async_engine = create_async_engine(
    url=settings.DB_ASYNC_URL,
    echo=True,
)
async_session_maker = async_sessionmaker(
    async_engine,
    expire_on_commit=False
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
