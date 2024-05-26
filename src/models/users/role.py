from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column

from db import Base, intpk

from schemas.users.role import RoleReadDTO


class Role(Base):
    __tablename__ = 'role'

    id: Mapped[intpk]
    title: Mapped[str] = mapped_column(unique=True)
    permissions = mapped_column(JSON, nullable=True)

    def to_read_model(self):
        return RoleReadDTO(**self.__dict__)

