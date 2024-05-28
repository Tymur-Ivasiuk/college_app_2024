from typing import Annotated, List
from fastapi import APIRouter, Depends

from services.users import StudentService
from api.dependencies.management_dependencies import student_service
from schemas.users.student import StudentReadDTO


student_router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@student_router.get('', response_model=List[StudentReadDTO])
async def get_all_students(student_service: Annotated[StudentService, Depends(student_service)]):
    students = await student_service.find_all()
    return students

