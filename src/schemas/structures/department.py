from pydantic import BaseModel


class DepartmentCreateDTO(BaseModel):
    title: str
    head_id: int


class DepartmentReadDTO(DepartmentCreateDTO):
    id: int
