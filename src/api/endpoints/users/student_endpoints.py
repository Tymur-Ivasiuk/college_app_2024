from typing import Annotated, List, Union
from fastapi import APIRouter, Depends

from services.users import StudentService
from api.dependencies.users_dependencies import student_service
from schemas.users.student import StudentReadDTO, StudentWithUserCreateDTO, StudentWithoutUserCreateDTO, \
    StudentReadRelDTO

student_router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@student_router.get('', response_model=List[StudentReadRelDTO])
async def get_all_students(student_service: Annotated[StudentService, Depends(student_service)]):
    students = await student_service.find_all()
    return students


@student_router.post("", response_model=StudentReadDTO)
async def add_department(
    student: Union[StudentWithUserCreateDTO, StudentWithoutUserCreateDTO],
    student_service: Annotated[StudentService, Depends(student_service)]
):
    student = await student_service.add_one(student)
    return student
