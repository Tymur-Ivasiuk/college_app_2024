from fastapi import HTTPException

from utils.repository_system import AbstractRepository
from schemas.learning_proccess.grade import GradeCreateDTO, GradeReadDTO, GradeUpdateDTO


class GradeService:
    def __init__(self, grade_repo: type[AbstractRepository]):
        self.grade_repo: AbstractRepository = grade_repo()

    async def find_all(self):
        grades = await self.grade_repo.find_all()
        return grades

    async def get_one(self, rec_id):
        grade = await self.grade_repo.get_one(
            rec_id=rec_id,
        )
        return grade

    async def add_one(self, grade_data: GradeCreateDTO):
        grade_dict = grade_data.model_dump()
        grade = await self.grade_repo.add_one(grade_dict)
        return grade

    async def update_by_id(self, rec_id: int, grade: GradeUpdateDTO):
        grade_dict = grade.model_dump(exclude_unset=True)

        update_grade_status = await self.grade_repo.update_by_id(
            rec_id,
            grade_dict,
        )
        if not update_grade_status:
            raise HTTPException(status_code=404, detail={
                "info": "No record to update"
            })

        grade = await self.get_one(rec_id=rec_id)
        return grade

    async def delete_by_id(self, rec_id: int):
        return await self.grade_repo.delete_by_id(rec_id)
    