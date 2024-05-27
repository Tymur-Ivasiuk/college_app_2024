from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base, intpk
from schemas.users.teacher import TeacherReadDTO


class Teacher(Base):
    __tablename__ = "teacher"

    id: Mapped[intpk]
    desc: Mapped[str] = mapped_column(nullable=True)  # example ("Math teacher")

    department_id: Mapped[int] = mapped_column(ForeignKey("department.id"))

    # One2One relationship
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="teacher")

    __table_args__ = (UniqueConstraint("user_id"),)

    def to_read_model(self):
        return TeacherReadDTO(
            id=self.id,
            first_name=self.user.first_name,
            last_name=self.user.last_name,
            patronymic=self.user.patronymic,
            email=self.user.email,
            is_active=self.user.is_active,
            is_superuser=self.user.is_superuser,
            is_verified=self.user.is_verified,
        )




