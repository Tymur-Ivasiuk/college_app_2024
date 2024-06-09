from pydantic import BaseModel
from datetime import date


class LectureCreateDTO(BaseModel):
    is_full_group: bool

    subject_id: int
    teacher_id: int | None = None
    classroom_id: int | None = None
    lecture_period_id: int
    group_id: int

    lection_date: date


class LectureUpdateDTO(LectureCreateDTO):
    is_full_group: bool | None = None

    subject_id: int | None = None
    teacher_id: int | None = None
    classroom_id: int | None = None
    lecture_period_id: int | None = None
    group_id: int | None = None

    lection_date: date | None = None


class LectureReadDTO(LectureCreateDTO):
    id: int
