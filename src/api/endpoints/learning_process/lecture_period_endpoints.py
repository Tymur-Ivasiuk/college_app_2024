from typing import List, Annotated

from fastapi import APIRouter, Depends

from api.dependencies.learning_proccess_dependencies import lecture_period_service
from services.learning_proccess import LecturePeriodService
from schemas.learning_proccess.lecture_period import LecturePeriodReadDTO, LecturePeriodCreateDTO, LecturePeriodUpdateDTO

lecture_period_router = APIRouter(
    prefix="/lecture_periods",
    tags=["LecturePeriods"],
)


@lecture_period_router.get("", response_model=List[LecturePeriodReadDTO])
async def get_lecture_periods(lecture_period_service: Annotated[LecturePeriodService, Depends(lecture_period_service)]):
    lecture_periods = await lecture_period_service.find_all()
    return lecture_periods


@lecture_period_router.get('/{rec_id}', response_model=LecturePeriodReadDTO)
async def get_lecture_period(rec_id: int, lecture_period_service: Annotated[LecturePeriodService, Depends(lecture_period_service)]):
    lecture_periods = await lecture_period_service.get_one(rec_id)
    return lecture_periods


@lecture_period_router.post("", response_model=LecturePeriodReadDTO)
async def add_lecture_period(
    lecture_period: LecturePeriodCreateDTO,
    lecture_period_service: Annotated[LecturePeriodService, Depends(lecture_period_service)]
):
    lecture_period = await lecture_period_service.add_one(lecture_period)
    return lecture_period


@lecture_period_router.put("/{rec_id}", response_model=LecturePeriodReadDTO)
async def update_lecture_period(
    rec_id: int,
    lecture_period: LecturePeriodUpdateDTO,
    lecture_period_service: Annotated[LecturePeriodService, Depends(lecture_period_service)]
):
    lecture_period = await lecture_period_service.update_by_id(rec_id, lecture_period)
    return lecture_period


@lecture_period_router.delete("/{rec_id}", response_model=bool)
async def delete_lecture_period(
    rec_id: int,
    lecture_period_service: Annotated[LecturePeriodService, Depends(lecture_period_service)]
):
    return await lecture_period_service.delete_by_id(rec_id)
