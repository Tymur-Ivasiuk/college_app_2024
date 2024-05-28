from typing import Optional

from pydantic import BaseModel

from ..structures.specialty import SpecialtyReadDTO
from ..users.teacher import TeacherReadDTO


class GroupCreateDTO(BaseModel):
    title: str
    full_title: str
    start_year: int

    curator_id: int
    specialty_id: int


class GroupReadDTO(GroupCreateDTO):
    id: int
    curator_id: Optional["TeacherReadDTO"] = None
    specialty_id: "SpecialtyReadDTO"


GroupReadDTO.update_forward_refs()
