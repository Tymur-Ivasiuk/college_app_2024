from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base, intpk
from schemas.users.student import StudentReadDTO


class Student(Base):
    __tablename__ = "student"

    id: Mapped[intpk]

    group_id: Mapped[int] = mapped_column(ForeignKey("group.id"))
    group: Mapped["Group"] = relationship("Group", back_populates="students")

    # One2One relationship
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["BaseUser"] = relationship("BaseUser", lazy="selectin")

    __table_args__ = (UniqueConstraint("user_id"),)

    def to_read_model(self):
        return StudentReadDTO(
            id=self.id,
            first_name=self.user.first_name,
            last_name=self.user.last_name,
            patronymic=self.user.patronymic,
            email=self.user.email,
            is_active=self.user.is_active,
            is_superuser=self.user.is_superuser,
            is_verified=self.user.is_verified,
            group_id=self.group_id
        )
