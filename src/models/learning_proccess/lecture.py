import enum

from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base, intpk


class LectureType(enum.Enum):
    lecture = "lecture"
    seminar = "seminar"
    webinar = "webinar"
    practice = "practice"


class Lecture(Base):
    __tablename__ = 'lecture'

    id: Mapped[intpk]

    is_full_group: Mapped[bool] = mapped_column(default=True)

    subject_id: Mapped[int] = mapped_column(ForeignKey('subject.id', ondelete='CASCADE'))
    teacher_id: Mapped[int | None] = mapped_column(ForeignKey('teacher.id', ondelete='SET NULL'), nullable=True)
    classroom_id: Mapped[int | None] = mapped_column(ForeignKey('classroom.id', ondelete="SET NULL"), nullable=True)
    lecture_period_id: Mapped[int] = mapped_column(ForeignKey('lecture_period.id'))
    group_id: Mapped[int] = mapped_column(ForeignKey('group.id'))

    lection_date: Mapped[date]



