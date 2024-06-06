from utils.repository_system import AbstractRepository
from schemas.structures.department import DepartmentCreateDTO


class DepartmentService:
    def __init__(self, department_repo: type[AbstractRepository]):
        self.department_repo: AbstractRepository = department_repo()

    async def find_all(self):
        departments = await self.department_repo.find_all()
        return departments

    async def add_one(self, department_data: DepartmentCreateDTO):
        department_dict = department_data.model_dump()
        department = await self.department_repo.add_one(department_dict)
        return department

    async def update_by_id(self, department_data: DepartmentCreateDTO):
        department_dict = department_data.model_dump()
        department = await self.department_repo.add_one(department_dict)
        return department
