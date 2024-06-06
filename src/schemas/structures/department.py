from pydantic import BaseModel


class DepartmentCreateDTO(BaseModel):
    title: str
    head_id: int


class DepartmentUpdateDTO(BaseModel):
    title: str | None = None
    head_id: int | None = None


class DepartmentReadDTO(DepartmentCreateDTO):
    id: int

    class Config:
        from_attributes = True
