from fastapi import HTTPException

from utils.repository_system import AbstractRepository
from schemas.learning_proccess.grade_event import GradeEventCreateDTO, GradeEventReadDTO, GradeEventUpdateDTO


class GradeEventService:
    def __init__(self, grade_event_repo: type[AbstractRepository]):
        self.grade_event_repo: AbstractRepository = grade_event_repo()

    async def find_all(self):
        grade_events = await self.grade_event_repo.find_all()
        return grade_events

    async def get_one(self, rec_id):
        grade_event = await self.grade_event_repo.get_one(
            rec_id=rec_id,
        )
        return grade_event

    async def add_one(self, grade_event_data: GradeEventCreateDTO):
        grade_event_dict = grade_event_data.model_dump()
        grade_event = await self.grade_event_repo.add_one(grade_event_dict)
        return grade_event

    async def update_by_id(self, rec_id: int, grade_event: GradeEventUpdateDTO):
        grade_event_dict = grade_event.model_dump(exclude_unset=True)

        update_grade_event_status = await self.grade_event_repo.update_by_id(
            rec_id,
            grade_event_dict,
        )
        if not update_grade_event_status:
            raise HTTPException(status_code=404, detail={
                "info": "No record to update"
            })

        grade_event = await self.get_one(rec_id=rec_id)
        return grade_event

    async def delete_by_id(self, rec_id: int):
        return await self.grade_event_repo.delete_by_id(rec_id)
