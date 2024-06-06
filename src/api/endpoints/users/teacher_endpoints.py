from typing import Annotated, List, Union
from fastapi import APIRouter, Depends

from api.dependencies.users_dependencies import teacher_service
from services.users.teacher import TeacherService
from schemas.users.teacher import (
    TeacherReadDTO,
    TeacherWithUserCreateDTO,
    TeacherWithoutUserCreateDTO,
    TeacherReadRelDTO, TeacherUpdateDTO
)

teacher_router = APIRouter(
    prefix="/teachers",
    tags=["Teachers"]
)


@teacher_router.get("", response_model=List[TeacherReadDTO])
async def get_all_teachers(teacher_service: Annotated[TeacherService, Depends(teacher_service)]):
    teachers = await teacher_service.find_all()
    return teachers


@teacher_router.get('/{rec_id}', response_model=TeacherReadRelDTO)
async def get_teacher(rec_id: int, teacher_service: Annotated[TeacherService, Depends(teacher_service)]):
    teachers = await teacher_service.get_one(rec_id)
    return teachers


@teacher_router.post("")
async def add_teacher(
    teacher: Union[TeacherWithUserCreateDTO, TeacherWithoutUserCreateDTO],
    teacher_service: Annotated[TeacherService, Depends(teacher_service)]
):
    teacher_id = await teacher_service.add_one(teacher)
    return teacher_id


@teacher_router.put("/{rec_id}", response_model=TeacherReadDTO)
async def update_teacher(
    rec_id: int,
    teacher: TeacherUpdateDTO,
    teacher_service: Annotated[TeacherService, Depends(teacher_service)]
):
    teacher = await teacher_service.update_by_id(rec_id, teacher)
    return teacher


@teacher_router.delete("/{rec_id}", response_model=bool)
async def delete_teacher(
    rec_id: int,
    teacher_service: Annotated[TeacherService, Depends(teacher_service)]
):
    return await teacher_service.delete_by_id(rec_id)
