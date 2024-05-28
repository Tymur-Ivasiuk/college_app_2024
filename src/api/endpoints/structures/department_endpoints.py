from typing import List, Annotated

from fastapi import APIRouter, Depends

from services.structures import DepartmentService
from api.dependencies.structures_dependencies import department_service
from schemas.structures.department import DepartmentReadDTO, DepartmentCreateDTO

department_router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)


@department_router.get("", response_model=List[DepartmentReadDTO])
async def get_departments(department_service: Annotated[DepartmentService, Depends(department_service)]):
    departments = await department_service.find_all()
    return departments


@department_router.post("", response_model=DepartmentReadDTO)
async def add_department(
    department_data: DepartmentCreateDTO,
    department_service: Annotated[DepartmentService, Depends(department_service)]
):
    department = await department_service.add_one(department_data)
    return department
