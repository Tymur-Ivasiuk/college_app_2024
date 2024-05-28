from fastapi import APIRouter

from .student_endpoints import student_router
from .teacher_endpoints import teacher_router

personal_router = APIRouter(
    prefix="/personal",
)

personal_router.include_router(student_router)
personal_router.include_router(teacher_router)
