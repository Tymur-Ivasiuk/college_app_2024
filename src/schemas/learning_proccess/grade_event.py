from pydantic import BaseModel
from datetime import date

from models.learning_proccess.grade_event import GradeType


class GradeEventCreateDTO(BaseModel):
    title: str
    grade_type: GradeType

    lection_id: int | None = None
    subject_id: int | None = None

    date_event: date


class GradeEventUpdateDTO(GradeEventCreateDTO):
    title: str | None = None
    grade_type: GradeType | None = None

    lection_id: int | None = None
    subject_id: int | None = None

    date_event: date | None = None


class GradeEventReadDTO(GradeEventCreateDTO):
    id: int
