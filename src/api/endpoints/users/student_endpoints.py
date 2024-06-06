from typing import Annotated, List, Union
from fastapi import APIRouter, Depends

from services.users import StudentService
from api.dependencies.users_dependencies import student_service
from schemas.users.student import (
    StudentReadDTO,
    StudentWithUserCreateDTO,
    StudentWithoutUserCreateDTO,
    StudentReadRelDTO,
    StudentUpdateDTO
)

student_router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@student_router.get('', response_model=List[StudentReadRelDTO])
async def get_all_students(student_service: Annotated[StudentService, Depends(student_service)]):
    students = await student_service.find_all()
    return students


@student_router.get('/{rec_id}', response_model=StudentReadRelDTO)
async def get_student(rec_id: int, student_service: Annotated[StudentService, Depends(student_service)]):
    students = await student_service.get_one(rec_id)
    return students


@student_router.post("", response_model=StudentReadDTO)
async def add_student(
    student: Union[StudentWithUserCreateDTO, StudentWithoutUserCreateDTO],
    student_service: Annotated[StudentService, Depends(student_service)]
):
    student = await student_service.add_one(student)
    return student


@student_router.put("/{rec_id}", response_model=StudentReadDTO)
async def update_student(
    rec_id: int,
    student: StudentUpdateDTO,
    student_service: Annotated[StudentService, Depends(student_service)]
):
    student = await student_service.update_by_id(rec_id, student)
    return student


@student_router.delete("/{rec_id}", response_model=bool)
async def delete_student(
    rec_id: int,
    student_service: Annotated[StudentService, Depends(student_service)]
):
    return await student_service.delete_by_id(rec_id)
