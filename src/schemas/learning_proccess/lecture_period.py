from pydantic import BaseModel


class LecturePeriodCreateDTO(BaseModel):
    title: str
    start_at: str
    end_at: str


class LecturePeriodUpdateDTO(LecturePeriodCreateDTO):
    title: str | None = None
    start_at: str | None = None
    end_at: str | None = None


class LecturePeriodReadDTO(LecturePeriodCreateDTO):
    id: int
