from fastapi import APIRouter

from .grade_endpoints import grade_router
from .grade_event_endpoints import grade_event_router
from .lecture_endpoints import lecture_router
from .lecture_period_endpoints import lecture_period_router
from .subject_endpoints import subject_router


learning_managment_router = APIRouter(
    prefix="/learning_managment"
)

learning_managment_router.include_router(grade_router)
learning_managment_router.include_router(grade_event_router)
learning_managment_router.include_router(lecture_router)
learning_managment_router.include_router(lecture_period_router)
learning_managment_router.include_router(subject_router)
