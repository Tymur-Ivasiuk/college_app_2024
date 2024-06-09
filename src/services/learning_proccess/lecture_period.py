from fastapi import HTTPException

from utils.repository_system import AbstractRepository
from schemas.learning_proccess.lecture_period import LecturePeriodCreateDTO, LecturePeriodReadDTO, LecturePeriodUpdateDTO


class LecturePeriodService:
    def __init__(self, lecture_period_repo: type[AbstractRepository]):
        self.lecture_period_repo: AbstractRepository = lecture_period_repo()

    async def find_all(self):
        lecture_periods = await self.lecture_period_repo.find_all()
        return lecture_periods

    async def get_one(self, rec_id):
        lecture_period = await self.lecture_period_repo.get_one(
            rec_id=rec_id,
        )
        return lecture_period

    async def add_one(self, lecture_period_data: LecturePeriodCreateDTO):
        lecture_period_dict = lecture_period_data.model_dump()
        lecture_period = await self.lecture_period_repo.add_one(lecture_period_dict)
        return lecture_period

    async def update_by_id(self, rec_id: int, lecture_period: LecturePeriodUpdateDTO):
        lecture_period_dict = lecture_period.model_dump(exclude_unset=True)

        update_lecture_period_status = await self.lecture_period_repo.update_by_id(
            rec_id,
            lecture_period_dict,
        )
        if not update_lecture_period_status:
            raise HTTPException(status_code=404, detail={
                "info": "No record to update"
            })

        lecture_period = await self.get_one(rec_id=rec_id)
        return lecture_period

    async def delete_by_id(self, rec_id: int):
        return await self.lecture_period_repo.delete_by_id(rec_id)
