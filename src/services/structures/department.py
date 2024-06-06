from fastapi import HTTPException

from utils.repository_system import AbstractRepository
from schemas.structures.department import DepartmentCreateDTO, DepartmentUpdateDTO


class DepartmentService:
    def __init__(self, department_repo: type[AbstractRepository]):
        self.department_repo: AbstractRepository = department_repo()

    async def find_all(self):
        departments = await self.department_repo.find_all()
        return departments
    
    async def get_one(self, rec_id):
        return await self.department_repo.get_one(rec_id)

    async def add_one(self, department_data: DepartmentCreateDTO):
        department_dict = department_data.model_dump()
        department = await self.department_repo.add_one(department_dict)
        return department

    async def update_by_id(self, rec_id: int, department: DepartmentUpdateDTO):
        department_dict = department.model_dump(exclude_unset=True)
        
        update_department_status = await self.department_repo.update_by_id(
            rec_id,
            department_dict,
        )
        if not update_department_status:
            raise HTTPException(status_code=404, detail={
                "info": "No record to update"
            })

        department = await self.get_one(rec_id=rec_id)
        return department

    async def delete_by_id(self, rec_id: int):
        return await self.department_repo.delete_by_id(rec_id)