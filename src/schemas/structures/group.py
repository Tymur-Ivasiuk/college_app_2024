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


class GroupUpdateDTO(BaseModel):
    title: str | None = None
    full_title: str | None = None
    start_year: int | None = None

    curator_id: int | None = None
    specialty_id: int | None = None


class GroupReadDTO(BaseModel):
    id: int
    title: str
    full_title: str
    start_year: int

    curator_id: Optional[int] = None
    specialty_id: int

    class Config:
        from_attributes = True


class GroupReadRelDTO(BaseModel):
    id: int
    title: str
    full_title: str
    start_year: int

    curator: Optional["TeacherReadDTO"] = None
    specialty: "SpecialtyReadDTO"

    class Config:
        from_attributes = True


GroupReadRelDTO.update_forward_refs()
