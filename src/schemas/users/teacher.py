from typing import Optional

from pydantic import BaseModel

from .base_user import BaseUserReadDTO, BaseUserCreateDTO
from ..structures.department import DepartmentReadDTO


class TeacherWithUserCreateDTO(BaseModel):
    user_id: int
    desc: Optional[str]
    department_id: Optional[int] = None


class TeacherWithoutUserCreateDTO(BaseUserCreateDTO):
    desc: Optional[str]
    department_id: Optional[int] = None


class TeacherReadDTO(BaseUserReadDTO):
    id: int
    desc: Optional[str] = None
    department_id: Optional["DepartmentReadDTO"] = None


TeacherReadDTO.update_forward_refs()
