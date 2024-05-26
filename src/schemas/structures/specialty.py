from typing import Optional
from pydantic import BaseModel


class SpecialtyCreateDTO(BaseModel):
    code: int
    title: str
    department_id: int | None


class SpecialtyReadDTO(SpecialtyCreateDTO):
    id: int
    department_id: Optional["DepartmentReadDTO"]

