from typing import List, Annotated

from fastapi import APIRouter, Depends

from api.dependencies.structures_dependencies import building_service
from services.structures import BuildingService
from schemas.structures.building import BuildingReadDTO, BuildingCreateDTO, BuildingUpdateDTO

building_router = APIRouter(
    prefix="/buildings",
    tags=["Buildings"],
)


@building_router.get("", response_model=List[BuildingReadDTO])
async def get_buildings(building_service: Annotated[BuildingService, Depends(building_service)]):
    buildings = await building_service.find_all()
    return buildings


@building_router.get('/{rec_id}', response_model=BuildingReadDTO)
async def get_building(rec_id: int, building_service: Annotated[BuildingService, Depends(building_service)]):
    buildings = await building_service.get_one(rec_id)
    return buildings


@building_router.post("", response_model=BuildingReadDTO)
async def add_building(
    building: BuildingCreateDTO,
    building_service: Annotated[BuildingService, Depends(building_service)]
):
    building = await building_service.add_one(building)
    return building


@building_router.put("/{rec_id}", response_model=BuildingReadDTO)
async def update_building(
    rec_id: int,
    building: BuildingUpdateDTO,
    building_service: Annotated[BuildingService, Depends(building_service)]
):
    building = await building_service.update_by_id(rec_id, building)
    return building


@building_router.delete("/{rec_id}", response_model=bool)
async def delete_building(
    rec_id: int,
    building_service: Annotated[BuildingService, Depends(building_service)]
):
    return await building_service.delete_by_id(rec_id)
