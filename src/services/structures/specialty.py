from utils.repository_system import AbstractRepository
from schemas.structures.specialty import SpecialtyCreateDTO


class SpecialtyService:
    def __init__(self, specialty_repo: type[AbstractRepository]):
        self.specialty_repo: AbstractRepository = specialty_repo()

    async def find_all(self):
        departments = await self.specialty_repo.find_all()
        return departments

    async def add_one(self, department_data: SpecialtyCreateDTO):
        department_dict = department_data.model_dump()
        department = await self.specialty_repo.add_one(department_dict)
        return department
