from typing import Optional

from pydantic import BaseModel

from .base_user import BaseUserReadDTO, BaseUserCreateDTO, BaseUserUpdateDTO
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
    department_id: Optional[int] = None

    class Config:
        from_attributes = True


class TeacherReadRelDTO(BaseUserReadDTO):
    id: int
    desc: Optional[str] = None
    department: Optional["DepartmentReadDTO"] = None

    class Config:
        from_attributes = True


class TeacherUpdateDTO(BaseUserUpdateDTO):
    desc: Optional[str] = None
    department_id: Optional[int] = None


class TeacherWithoutUserUpdateDTO(BaseModel):
    desc: Optional[str] = None
    department_id: Optional[int] = None


TeacherReadRelDTO.update_forward_refs()
