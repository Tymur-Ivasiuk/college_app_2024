from typing import Union

from utils.repository_system import AbstractRepository
from schemas.users.teacher import TeacherWithUserCreateDTO, TeacherWithoutUserCreateDTO, TeacherReadDTO

from .base_user import BaseUserServiceMixin


class TeacherService(BaseUserServiceMixin):
    def __init__(self, teacher_repo: type[AbstractRepository]):
        self.teacher_repo: AbstractRepository = teacher_repo()

    async def find_all(self):
        teachers = await self.teacher_repo.find_all()
        return teachers

    async def add_one(self, teacher: Union[TeacherWithUserCreateDTO, TeacherWithoutUserCreateDTO]):
        teacher_dict = teacher.model_dump()

        if not teacher_dict.get("user_id"):
            teacher_dict["user_id"] = await self._create_user(teacher_dict)

        teacher_create_dict = TeacherWithUserCreateDTO(**teacher_dict).model_dump()
        teacher_id = await self.teacher_repo.add_one(teacher_create_dict)
        return teacher_id
