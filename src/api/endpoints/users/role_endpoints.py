from typing import List, Annotated

from fastapi import APIRouter, Depends
from schemas.users.role import RoleCreateDTO, RoleReadDTO

from services.users import RoleService
from api.dependencies.users_dependencies import role_service

role_router = APIRouter(
    prefix="/roles",
    tags=["Roles"],
)


@role_router.post("")
async def add_role(role: RoleCreateDTO, role_service: Annotated[RoleService, Depends(role_service)]):
    role_id = await role_service.add_role(role)
    return {
        "role_id": role_id,
    }


@role_router.get("", response_model=List[RoleReadDTO])
async def get_all_roles(role_service: Annotated[RoleService, Depends(role_service)]):
    roles = await role_service.find_all()
    return roles
