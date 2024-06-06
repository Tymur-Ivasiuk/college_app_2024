from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base, intpk, str50
from schemas.structures.department import DepartmentReadDTO


class Department(Base):
    __tablename__ = "department"

    id: Mapped[intpk]
    title: Mapped[str50]
    head_id: Mapped[int] = mapped_column(ForeignKey('teacher.id'))

    # Meny2One relationship
    teachers: Mapped["Teacher"] = relationship(
        "Teacher", back_populates="department", foreign_keys="Teacher.department_id")

    def to_read_model(self):
        return DepartmentReadDTO(**self.__dict__)


