from pydantic import BaseModel
from .department import DepartmentReadDTO


class SpecialtyCreateDTO(BaseModel):
    code: int
    title: str
    department_id: int | None


class SpecialtyReadDTO(BaseModel):
    id: int
    code: int
    title: str
    department_id: int

    class Config:
        from_attributes = True


class SpecialtyReadRelDTO(BaseModel):
    id: int
    code: int
    title: str
    department: "DepartmentReadDTO"

    class Config:
        from_attributes = True


SpecialtyReadRelDTO.update_forward_refs()
