from typing import Union

from fastapi import HTTPException

from schemas.users.base_user import BaseUserUpdateDTO
from schemas.users.student import (
    StudentWithUserCreateDTO,
    StudentWithoutUserCreateDTO,
    StudentReadRelDTO,
    StudentUpdateDTO,
    StudentWithoutUserUpdateDTO
)
from utils.repository_system import AbstractRepository

from .base_user import BaseUserServiceMixin


class StudentService(BaseUserServiceMixin):
    def __init__(self, student_repo: type[AbstractRepository], user_repo: type[AbstractRepository]):
        self.student_repo: AbstractRepository = student_repo()
        self.user_repo: AbstractRepository = user_repo()

    async def find_all(self):
        students = await self.student_repo.find_all(
            selectin_field_names=['group'],
            to_read_model=False
        )
        students_data = [
            StudentReadRelDTO.model_validate(group).model_dump()
            for group in students
        ]
        return students_data

    async def get_one(self, rec_id):
        student = await self.student_repo.get_one(
            rec_id,
            to_read_model=False,
            selectin_field_names=['group'],
        )
        return student

    async def add_one(self, student: Union[StudentWithUserCreateDTO, StudentWithoutUserCreateDTO]):
        student_dict = student.model_dump()

        if not student_dict.get("user_id"):
            student_dict["user_id"] = await self._create_user(student_dict)

        student_create_dict = StudentWithUserCreateDTO(**student_dict).model_dump()
        student = await self.student_repo.add_one(student_create_dict)
        return student

    async def update_by_id(self, rec_id: int, student: StudentUpdateDTO):
        data = student.model_dump(exclude_unset=True)
        user_dict = BaseUserUpdateDTO(**data).model_dump(exclude_unset=True)
        student_dict = StudentWithoutUserUpdateDTO(**data).model_dump(exclude_unset=True)

        if user_dict:
            student = await self.get_one(rec_id=rec_id)
            await self.user_repo.update_by_id(student.user_id, user_dict)

        update_student_status = await self.student_repo.update_by_id(
            rec_id,
            student_dict,
        )
        if not update_student_status:
            raise HTTPException(status_code=404, detail={
                "info": "No record to update"
            })

        student = await self.get_one(rec_id=rec_id)
        return student

    async def delete_by_id(self, rec_id: int):
        return await self.student_repo.delete_by_id(rec_id)