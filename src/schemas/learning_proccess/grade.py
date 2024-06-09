from pydantic import BaseModel
from models.learning_proccess.grade import MarkType


class GradeCreateDTO(BaseModel):
    desc: int | None = None

    grade_event_id: int
    student_id: int
    teacher_id: int

    mark_type: MarkType
    mark: int


class GradeUpdateDTO(GradeCreateDTO):
    desc: int | None = None

    grade_event_id: int | None = None
    student_id: int | None = None
    teacher_id: int | None = None

    mark_type: MarkType | None = None
    mark: int | None = None


class GradeReadDTO(GradeCreateDTO):
    id: int
