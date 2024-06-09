from typing import List, Annotated

from fastapi import APIRouter, Depends

from services.learning_proccess.grade import GradeService
from schemas.learning_proccess.grade import GradeUpdateDTO, GradeReadDTO, GradeCreateDTO
from api.dependencies.learning_proccess_dependencies import grade_service


grade_router = APIRouter(
    prefix="/grades",
    tags=["Grades"],
)


@grade_router.get("", response_model=List[GradeReadDTO])
async def get_grades(grade_service: Annotated[GradeService, Depends(grade_service)]):
    grades = await grade_service.find_all()
    return grades


@grade_router.get('/{rec_id}', response_model=GradeReadDTO)
async def get_grade(rec_id: int, grade_service: Annotated[GradeService, Depends(grade_service)]):
    grades = await grade_service.get_one(rec_id)
    return grades


@grade_router.post("", response_model=GradeReadDTO)
async def add_grade(
    grade: GradeCreateDTO,
    grade_service: Annotated[GradeService, Depends(grade_service)]
):
    grade = await grade_service.add_one(grade)
    return grade


@grade_router.put("/{rec_id}", response_model=GradeReadDTO)
async def update_grade(
    rec_id: int,
    grade: GradeUpdateDTO,
    grade_service: Annotated[GradeService, Depends(grade_service)]
):
    grade = await grade_service.update_by_id(rec_id, grade)
    return grade


@grade_router.delete("/{rec_id}", response_model=bool)
async def delete_grade(
    rec_id: int,
    grade_service: Annotated[GradeService, Depends(grade_service)]
):
    return await grade_service.delete_by_id(rec_id)
