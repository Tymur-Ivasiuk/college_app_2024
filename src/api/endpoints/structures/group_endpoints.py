from typing import List, Annotated

from fastapi import APIRouter, Depends

from api.dependencies.structures_dependencies import group_service
from services.structures import GroupService
from schemas.structures.group import GroupReadDTO, GroupCreateDTO, GroupReadRelDTO, GroupUpdateDTO

group_router = APIRouter(
    prefix="/groups",
    tags=["Groups"],
)


@group_router.get("", response_model=List[GroupReadRelDTO])
async def get_groups(group_service: Annotated[GroupService, Depends(group_service)]):
    groups = await group_service.find_all()
    return groups


@group_router.get('/{rec_id}', response_model=GroupReadRelDTO)
async def get_group(rec_id: int, group_service: Annotated[GroupService, Depends(group_service)]):
    groups = await group_service.get_one(rec_id)
    return groups


@group_router.post("", response_model=GroupReadDTO)
async def add_group(
    group: GroupCreateDTO,
    group_service: Annotated[GroupService, Depends(group_service)]
):
    group = await group_service.add_one(group)
    return group


@group_router.put("/{rec_id}", response_model=GroupReadRelDTO)
async def update_group(
    rec_id: int,
    group: GroupUpdateDTO,
    group_service: Annotated[GroupService, Depends(group_service)]
):
    group = await group_service.update_by_id(rec_id, group)
    return group


@group_router.delete("/{rec_id}", response_model=bool)
async def delete_group(
    rec_id: int,
    group_service: Annotated[GroupService, Depends(group_service)]
):
    return await group_service.delete_by_id(rec_id)
