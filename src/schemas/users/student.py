from pydantic import BaseModel

from .base_user import BaseUserReadDTO, BaseUserCreateDTO
from ..structures.group import GroupReadDTO


class StudentWithUserCreateDTO(BaseModel):
    user_id: int
    group_id: int


class StudentWithoutUserCreateDTO(BaseUserCreateDTO):
    group_id: int


class StudentReadDTO(BaseUserReadDTO):
    id: int
    group_id: int


class StudentReadRelDTO(BaseUserReadDTO):
    id: int
    group: "GroupReadDTO"


StudentReadRelDTO.update_forward_refs()
