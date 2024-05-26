from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from sqlalchemy import String, Boolean, JSON, ForeignKey, Integer, MetaData, Table, Column
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Role(Base):
    __tablename__ = 'role'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    permissions = mapped_column(JSON, nullable=True)


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)

    first_name: Mapped[str] = mapped_column(String(length=50))
    last_name: Mapped[str] = mapped_column(String(length=50))
    patronymic: Mapped[str] = mapped_column(String(length=50))

    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    role_id: Mapped[int] = mapped_column(Integer, ForeignKey('role.id'))
