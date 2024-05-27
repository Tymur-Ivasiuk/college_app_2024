from pydantic import BaseModel
from .department import DepartmentReadDTO


class SpecialtyCreateDTO(BaseModel):
    code: int
    title: str
    department_id: int | None


class SpecialtyReadDTO(SpecialtyCreateDTO):
    id: int
    department_id: "DepartmentReadDTO" = None


SpecialtyReadDTO.update_forward_refs()
