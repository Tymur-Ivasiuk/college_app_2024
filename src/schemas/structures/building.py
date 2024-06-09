from pydantic import BaseModel


class BuildingCreateDTO(BaseModel):
    title: str
    address: str

    lat: float
    lng: float


class BuildingUpdateDTO(BuildingCreateDTO):
    title: str | None = None
    address: str | None = None

    lat: float | None = None
    lng: float | None = None


class BuildingReadDTO(BuildingCreateDTO):
    id: int
