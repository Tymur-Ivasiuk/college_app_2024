from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base, intpk
from schemas.learning_proccess.group import GroupReadDTO


class Group(Base):
    __tablename__ = "group"

    # TODO: create autogenerate title (exp. `41-KH`)

    id: Mapped[intpk]
    title: Mapped[str] = mapped_column(String(10))  # maybe unique?
    full_title: Mapped[str | None] = mapped_column(nullable=True)
    start_year: Mapped[int]

    curator_id: Mapped[int | None] = mapped_column(
        ForeignKey("teacher.id", ondelete="SET NULL"), nullable=True)
    specialty_id: Mapped[int] = mapped_column(
        ForeignKey("specialty.id", ondelete="CASCADE"))

    students: Mapped["Student"] = relationship("Student", back_populates="group")

    def to_read_model(self):
        return GroupReadDTO(**self.__dict__)
