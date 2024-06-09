from typing import List, Annotated

from fastapi import APIRouter, Depends

from api.dependencies.learning_proccess_dependencies import lecture_service
from services.learning_proccess import LectureService
from schemas.learning_proccess.lecture import LectureReadDTO, LectureCreateDTO, LectureUpdateDTO

lecture_router = APIRouter(
    prefix="/lectures",
    tags=["Lectures"],
)


@lecture_router.get("", response_model=List[LectureReadDTO])
async def get_lectures(lecture_service: Annotated[LectureService, Depends(lecture_service)]):
    lectures = await lecture_service.find_all()
    return lectures


@lecture_router.get('/{rec_id}', response_model=LectureReadDTO)
async def get_lecture(rec_id: int, lecture_service: Annotated[LectureService, Depends(lecture_service)]):
    lectures = await lecture_service.get_one(rec_id)
    return lectures


@lecture_router.post("", response_model=LectureReadDTO)
async def add_lecture(
    lecture: LectureCreateDTO,
    lecture_service: Annotated[LectureService, Depends(lecture_service)]
):
    lecture = await lecture_service.add_one(lecture)
    return lecture


@lecture_router.put("/{rec_id}", response_model=LectureReadDTO)
async def update_lecture(
    rec_id: int,
    lecture: LectureUpdateDTO,
    lecture_service: Annotated[LectureService, Depends(lecture_service)]
):
    lecture = await lecture_service.update_by_id(rec_id, lecture)
    return lecture


@lecture_router.delete("/{rec_id}", response_model=bool)
async def delete_lecture(
    rec_id: int,
    lecture_service: Annotated[LectureService, Depends(lecture_service)]
):
    return await lecture_service.delete_by_id(rec_id)
