import enum

from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base, intpk, str50


class GradeType(enum.Enum):
    lecture_grade = "lecture_grade"
    semester_grade = "semester_grade"
    module_grade = "module_grade"
    control_grade = "control_grade"
    independent_work_grade = "independent_work_grade"
    default_grade = "default_grade"


class GradeEvent(Base):
    __tablename__ = "grade_event"

    id: Mapped[intpk]

    title: Mapped[str50]
    grade_type: Mapped[GradeType] = mapped_column(default=GradeType.lecture_grade)

    lection_id: Mapped[int | None] = mapped_column(ForeignKey('lecture.id', ondelete="SET NULL"), nullable=True)
    subject_id: Mapped[int | None] = mapped_column(ForeignKey('subject.id', ondelete="SET NULL"))

    date_event: Mapped[date]







