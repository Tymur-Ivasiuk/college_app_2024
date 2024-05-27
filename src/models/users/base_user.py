from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from sqlalchemy import String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from db import Base, intpk, str50, updated_at, created_at
from schemas.users.base_user import BaseUserReadDTO


class BaseUser(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'user'

    id: Mapped[intpk]

    first_name: Mapped[str50]
    last_name: Mapped[str50]
    patronymic: Mapped[str50]

    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    role_id: Mapped[int] = mapped_column(Integer, ForeignKey('role.id'))

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    # TODO: check how works
    def to_read_model(self):
        return BaseUserReadDTO(**self.__dict__)
