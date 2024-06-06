from typing import List, Annotated

from fastapi import APIRouter, Depends

from services.structures import DepartmentService
from api.dependencies.structures_dependencies import department_service
from schemas.structures.department import DepartmentReadDTO, DepartmentCreateDTO, DepartmentUpdateDTO

department_router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)


@department_router.get("", response_model=List[DepartmentReadDTO])
async def get_departments(department_service: Annotated[DepartmentService, Depends(department_service)]):
    departments = await department_service.find_all()
    return departments


@department_router.get('/{rec_id}', response_model=DepartmentReadDTO)
async def get_department(rec_id: int, department_service: Annotated[DepartmentService, Depends(department_service)]):
    departments = await department_service.get_one(rec_id)
    return departments


@department_router.post("", response_model=DepartmentReadDTO)
async def add_department(
    department_data: DepartmentCreateDTO,
    department_service: Annotated[DepartmentService, Depends(department_service)]
):
    department = await department_service.add_one(department_data)
    return department


@department_router.put("/{rec_id}", response_model=DepartmentReadDTO)
async def update_department(
    rec_id: int,
    department: DepartmentUpdateDTO,
    department_service: Annotated[DepartmentService, Depends(department_service)]
):
    department = await department_service.update_by_id(rec_id, department)
    return department


@department_router.delete("/{rec_id}", response_model=bool)
async def delete_department(
    rec_id: int,
    department_service: Annotated[DepartmentService, Depends(department_service)]
):
    return await department_service.delete_by_id(rec_id)