from fastapi import HTTPException

from utils.repository_system import AbstractRepository
from schemas.structures.classroom import ClassroomCreateDTO, ClassroomReadDTO, ClassroomUpdateDTO


class ClassroomService:
    def __init__(self, classroom_repo: type[AbstractRepository]):
        self.classroom_repo: AbstractRepository = classroom_repo()

    async def find_all(self):
        classrooms = await self.classroom_repo.find_all()
        return classrooms

    async def get_one(self, rec_id):
        classroom = await self.classroom_repo.get_one(
            rec_id=rec_id,
        )
        return classroom

    async def add_one(self, classroom_data: ClassroomCreateDTO):
        classroom_dict = classroom_data.model_dump()
        classroom = await self.classroom_repo.add_one(classroom_dict)
        return classroom

    async def update_by_id(self, rec_id: int, classroom: ClassroomUpdateDTO):
        classroom_dict = classroom.model_dump(exclude_unset=True)

        update_classroom_status = await self.classroom_repo.update_by_id(
            rec_id,
            classroom_dict,
        )
        if not update_classroom_status:
            raise HTTPException(status_code=404, detail={
                "info": "No record to update"
            })

        classroom = await self.get_one(rec_id=rec_id)
        return classroom

    async def delete_by_id(self, rec_id: int):
        return await self.classroom_repo.delete_by_id(rec_id)
