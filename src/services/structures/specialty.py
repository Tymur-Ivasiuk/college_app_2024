from fastapi import HTTPException

from utils.repository_system import AbstractRepository
from schemas.structures.specialty import SpecialtyCreateDTO, SpecialtyUpdateDTO


class SpecialtyService:
    def __init__(self, specialty_repo: type[AbstractRepository]):
        self.specialty_repo: AbstractRepository = specialty_repo()

    async def find_all(self):
        specialtys = await self.specialty_repo.find_all()
        return specialtys
    
    async def get_one(self, rec_id):
        return await self.specialty_repo.get_one(rec_id)

    async def add_one(self, specialty_data: SpecialtyCreateDTO):
        specialty_dict = specialty_data.model_dump()
        specialty = await self.specialty_repo.add_one(specialty_dict)
        return specialty

    async def update_by_id(self, rec_id: int, specialty: SpecialtyUpdateDTO):
        specialty_dict = specialty.model_dump(exclude_unset=True)

        update_specialty_status = await self.specialty_repo.update_by_id(
            rec_id,
            specialty_dict,
        )
        if not update_specialty_status:
            raise HTTPException(status_code=404, detail={
                "info": "No record to update"
            })

        specialty = await self.get_one(rec_id=rec_id)
        return specialty

    async def delete_by_id(self, rec_id: int):
        return await self.specialty_repo.delete_by_id(rec_id)
