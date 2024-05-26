from typing import Optional
from pydantic import BaseModel


class GroupCreateDTO(BaseModel):
    title: str
    full_title: str
    start_year: int

    curator_id: int
    specialty_id: int


class GroupReadDTO(GroupCreateDTO):
    id: int
    curator_id: Optional["TeacherReadDTO"]
    specialty_id: "SpecialtyReadDTO"
