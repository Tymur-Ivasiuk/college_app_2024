from typing import Annotated, List, Union
from fastapi import APIRouter, Depends

from api.dependencies.users_dependencies import teacher_service
from services.users.teacher import TeacherService
from schemas.users.teacher import TeacherReadDTO, TeacherWithUserCreateDTO, TeacherWithoutUserCreateDTO


teacher_router = APIRouter(
    prefix="/teachers",
    tags=["Teachers"]
)


@teacher_router.get("", response_model=List[TeacherReadDTO])
async def get_all_teachers(teacher_service: Annotated[TeacherService, Depends(teacher_service)]):
    teachers = await teacher_service.find_all()
    return teachers


@teacher_router.post("")
async def add_teacher(
    teacher: Union[TeacherWithUserCreateDTO, TeacherWithoutUserCreateDTO],
    teacher_service: Annotated[TeacherService, Depends(teacher_service)]
):
    teacher_id = await teacher_service.add_one(teacher)
    return teacher_id
