import enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates
from db import Base, intpk, str50


class MarkType(enum.Enum):
    mark100 = "mark100"
    mark12 = "mark12"


class Grade(Base):
    __tablename__ = "grade"

    id: Mapped[intpk]
    desc: Mapped[str | None] = mapped_column(nullable=True)

    grade_event_id: Mapped[int] = mapped_column(ForeignKey('grade_event.id'))
    student_id: Mapped[int] = mapped_column(ForeignKey('student.id', ondelete='SET NULL'))
    teacher_id: Mapped[int] = mapped_column(ForeignKey('teacher.id', ondelete='SET NULL'))

    mark_type: Mapped[MarkType] = mapped_column(default=MarkType.mark100)
    mark: Mapped[int]

    @validates('mark')
    def validate_name(self, key, value):
        assert value >= 0
        assert value <= 100
        return value
    



