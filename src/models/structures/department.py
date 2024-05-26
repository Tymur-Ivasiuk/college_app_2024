from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base, intpk, str50
from schemas.structures import DepartmentReadDTO


class Department(Base):
    __tablename__ = "department"

    id: Mapped[intpk]
    title: Mapped[str50]
    head_id: Mapped[int] = mapped_column(ForeignKey('teacher.id'))

    # Meny2One relationship
    teacher_ids: Mapped[list["Teacher"]] = relationship(back_populates="department_id")

    def to_read_model(self):
        return DepartmentReadDTO(**self.__dict__)


