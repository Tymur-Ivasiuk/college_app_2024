from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db import Base, intpk
from schemas.structures.specialty import SpecialtyReadDTO


class Specialty(Base):
    __tablename__ = "specialty"

    id: Mapped[intpk]
    code: Mapped[int] = mapped_column(unique=True)
    title: Mapped[str] = mapped_column(unique=True)

    department_id: Mapped[int | None] = mapped_column(ForeignKey("department.id", ondelete="SET NULL"), nullable=True)

    def to_read_model(self):
        return SpecialtyReadDTO(**self.__dict__)
