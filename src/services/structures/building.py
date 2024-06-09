from fastapi import HTTPException

from utils.repository_system import AbstractRepository
from schemas.structures.building import BuildingCreateDTO, BuildingReadDTO, BuildingUpdateDTO


class BuildingService:
    def __init__(self, building_repo: type[AbstractRepository]):
        self.building_repo: AbstractRepository = building_repo()

    async def find_all(self):
        buildings = await self.building_repo.find_all()
        return buildings

    async def get_one(self, rec_id):
        building = await self.building_repo.get_one(
            rec_id=rec_id,
        )
        return building

    async def add_one(self, building_data: BuildingCreateDTO):
        building_dict = building_data.model_dump()
        building = await self.building_repo.add_one(building_dict)
        return building

    async def update_by_id(self, rec_id: int, building: BuildingUpdateDTO):
        building_dict = building.model_dump(exclude_unset=True)

        update_building_status = await self.building_repo.update_by_id(
            rec_id,
            building_dict,
        )
        if not update_building_status:
            raise HTTPException(status_code=404, detail={
                "info": "No record to update"
            })

        building = await self.get_one(rec_id=rec_id)
        return building

    async def delete_by_id(self, rec_id: int):
        return await self.building_repo.delete_by_id(rec_id)
