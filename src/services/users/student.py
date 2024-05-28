from typing import Union

from schemas.users.student import StudentWithUserCreateDTO, StudentWithoutUserCreateDTO
from utils.repository_system import AbstractRepository

from .base_user import BaseUserServiceMixin


class StudentService(BaseUserServiceMixin):
    def __init__(self, student_repo: type[AbstractRepository]):
        self.student_repo: AbstractRepository = student_repo()

    async def find_all(self):
        students = await self.student_repo.find_all()
        return students

    async def add_one(self, teacher: Union[StudentWithUserCreateDTO, StudentWithoutUserCreateDTO]):
        student_dict = teacher.model_dump()

        if not student_dict.get("user_id"):
            student_dict["user_id"] = await self._create_user(student_dict)

        student_create_dict = StudentWithUserCreateDTO(**student_dict).model_dump()
        student = await self.student_repo.add_one(student_create_dict)
        return student
