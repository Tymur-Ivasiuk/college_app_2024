from fastapi import HTTPException

from utils.repository_system import AbstractRepository
from schemas.learning_proccess.lecture import LectureCreateDTO, LectureReadDTO, LectureUpdateDTO


class LectureService:
    def __init__(self, lecture_repo: type[AbstractRepository]):
        self.lecture_repo: AbstractRepository = lecture_repo()

    async def find_all(self):
        lectures = await self.lecture_repo.find_all()
        return lectures

    async def get_one(self, rec_id):
        lecture = await self.lecture_repo.get_one(
            rec_id=rec_id,
        )
        return lecture

    async def add_one(self, lecture_data: LectureCreateDTO):
        lecture_dict = lecture_data.model_dump()
        lecture = await self.lecture_repo.add_one(lecture_dict)
        return lecture

    async def update_by_id(self, rec_id: int, lecture: LectureUpdateDTO):
        lecture_dict = lecture.model_dump(exclude_unset=True)

        update_lecture_status = await self.lecture_repo.update_by_id(
            rec_id,
            lecture_dict,
        )
        if not update_lecture_status:
            raise HTTPException(status_code=404, detail={
                "info": "No record to update"
            })

        lecture = await self.get_one(rec_id=rec_id)
        return lecture

    async def delete_by_id(self, rec_id: int):
        return await self.lecture_repo.delete_by_id(rec_id)
