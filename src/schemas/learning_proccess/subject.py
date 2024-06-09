from pydantic import BaseModel


class SubjectCreateDTO(BaseModel):
    title: str
    is_professional: bool


class SubjectUpdateDTO(SubjectCreateDTO):
    title: str | None = None
    is_professional: bool | None = None


class SubjectReadDTO(SubjectCreateDTO):
    id: int
