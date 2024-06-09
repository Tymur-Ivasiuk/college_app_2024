from pydantic import BaseModel


class ClassroomCreateDTO(BaseModel):
    title: str
    max_student_capacity: int
    features: str | None = None

    building_id: int


class ClassroomUpdateDTO(ClassroomCreateDTO):
    title: str | None = None
    max_student_capacity: int | None = None
    features: str | None = None

    building_id: int | None = None


class ClassroomReadDTO(ClassroomCreateDTO):
    id: int
