from typing import List, Annotated

from fastapi import APIRouter, Depends

from api.dependencies.structures_dependencies import group_service
from services.structures import GroupService
from schemas.structures.group import GroupReadDTO, GroupCreateDTO, GroupReadRelDTO

group_router = APIRouter(
    prefix="/groups",
    tags=["Groups"],
)


@group_router.get("", response_model=List[GroupReadRelDTO])
async def get_groups(group_service: Annotated[GroupService, Depends(group_service)]):
    groups = await group_service.find_all()
    return groups


@group_router.post("", response_model=GroupReadDTO)
async def add_group(
    group: GroupCreateDTO,
    group_service: Annotated[GroupService, Depends(group_service)]
):
    group = await group_service.add_one(group)
    return group
