from typing import Union

from fastapi import HTTPException

from schemas.users.base_user import BaseUserUpdateDTO
from utils.repository_system import AbstractRepository
from schemas.users.teacher import TeacherWithUserCreateDTO, TeacherWithoutUserCreateDTO, TeacherReadDTO, \
    TeacherUpdateDTO, TeacherWithoutUserUpdateDTO

from .base_user import BaseUserServiceMixin


class TeacherService(BaseUserServiceMixin):
    def __init__(self, teacher_repo: type[AbstractRepository], user_repo: type[AbstractRepository]):
        self.teacher_repo: AbstractRepository = teacher_repo()
        self.user_repo: AbstractRepository = user_repo()

    async def find_all(self):
        teachers = await self.teacher_repo.find_all()
        return teachers
    
    async def get_one(self, rec_id):
        teacher = await self.teacher_repo.get_one(
            rec_id,
            to_read_model=False,
            selectin_field_names=["department"]
        )
        return teacher

    async def add_one(self, teacher: Union[TeacherWithUserCreateDTO, TeacherWithoutUserCreateDTO]):
        teacher_dict = teacher.model_dump()

        if not teacher_dict.get("user_id"):
            teacher_dict["user_id"] = await self._create_user(teacher_dict)

        teacher_create_dict = TeacherWithUserCreateDTO(**teacher_dict).model_dump()
        teacher = await self.teacher_repo.add_one(teacher_create_dict)
        return teacher

    async def update_by_id(self, rec_id: int, teacher: TeacherUpdateDTO):
        data = teacher.model_dump(exclude_unset=True)
        user_dict = BaseUserUpdateDTO(**data).model_dump(exclude_unset=True)
        teacher_dict = TeacherWithoutUserUpdateDTO(**data).model_dump(exclude_unset=True)

        if user_dict:
            teacher = await self.get_one(rec_id=rec_id)
            await self.user_repo.update_by_id(teacher.user_id, user_dict)

        update_teacher_status = await self.teacher_repo.update_by_id(
            rec_id,
            teacher_dict,
        )
        if not update_teacher_status:
            raise HTTPException(status_code=404, detail={
                "info": "No record to update"
            })

        teacher = await self.get_one(rec_id=rec_id)
        return teacher

    async def delete_by_id(self, rec_id: int):
        return await self.teacher_repo.delete_by_id(rec_id)