from utils.repository_system import AbstractRepository


class TeacherService:
    def __init__(self, teacher_repo: type[AbstractRepository]):
        self.teacher_repo: AbstractRepository = teacher_repo()

    async def find_all(self):
        teachers = await self.teacher_repo.find_all()
        return teachers

