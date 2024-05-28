from fastapi import APIRouter
from .department_endpoints import department_router


structures_router = APIRouter(
    prefix="/structures",
)

structures_router.include_router(department_router)
