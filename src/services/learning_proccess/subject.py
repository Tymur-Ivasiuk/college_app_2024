from fastapi import HTTPException

from utils.repository_system import AbstractRepository
from schemas.learning_proccess.subject import SubjectCreateDTO, SubjectReadDTO, SubjectUpdateDTO


class SubjectService:
    def __init__(self, subject_repo: type[AbstractRepository]):
        self.subject_repo: AbstractRepository = subject_repo()

    async def find_all(self):
        subjects = await self.subject_repo.find_all()
        return subjects

    async def get_one(self, rec_id):
        subject = await self.subject_repo.get_one(
            rec_id=rec_id,
        )
        return subject

    async def add_one(self, subject_data: SubjectCreateDTO):
        subject_dict = subject_data.model_dump()
        subject = await self.subject_repo.add_one(subject_dict)
        return subject

    async def update_by_id(self, rec_id: int, subject: SubjectUpdateDTO):
        subject_dict = subject.model_dump(exclude_unset=True)

        update_subject_status = await self.subject_repo.update_by_id(
            rec_id,
            subject_dict,
        )
        if not update_subject_status:
            raise HTTPException(status_code=404, detail={
                "info": "No record to update"
            })

        subject = await self.get_one(rec_id=rec_id)
        return subject

    async def delete_by_id(self, rec_id: int):
        return await self.subject_repo.delete_by_id(rec_id)
