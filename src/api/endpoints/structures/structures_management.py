from fastapi import APIRouter

from .department_endpoints import department_router
from .specialty_endpoints import specialty_router
from .group_endpoints import group_router


structures_router = APIRouter(
    prefix="/structures",
)

structures_router.include_router(department_router)
structures_router.include_router(specialty_router)
structures_router.include_router(group_router)
