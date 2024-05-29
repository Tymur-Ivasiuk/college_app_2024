from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base, intpk
from schemas.structures.group import GroupReadDTO


class Group(Base):
    __tablename__ = "group"

    # TODO: create autogenerate title (exp. `41-KH`)

    id: Mapped[intpk]
    title: Mapped[str] = mapped_column(String(10))  # maybe unique?
    full_title: Mapped[str | None] = mapped_column(nullable=True)
    start_year: Mapped[int]

    curator_id: Mapped[int | None] = mapped_column(
        ForeignKey("teacher.id", ondelete="SET NULL"), nullable=True)
    curator: Mapped["Teacher"] = relationship("Teacher")
    specialty_id: Mapped[int] = mapped_column(
        ForeignKey("specialty.id", ondelete="CASCADE"))
    specialty: Mapped["Specialty"] = relationship("Specialty")

    students: Mapped["Student"] = relationship("Student", back_populates="group")

    def to_read_model(self):
        return GroupReadDTO(
            id=self.id,
            title=self.title,
            full_title=self.full_title,
            start_year=self.start_year,
            curator_id=self.curator_id,
            specialty_id=self.specialty_id
        )
