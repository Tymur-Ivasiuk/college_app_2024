from utils.repository_system import AbstractRepository


class StudentService:
    def __init__(self, student_repo: type[AbstractRepository]):
        self.student_repo: AbstractRepository = student_repo()

    async def find_all(self):
        students = await self.student_repo.find_all()
        return students
