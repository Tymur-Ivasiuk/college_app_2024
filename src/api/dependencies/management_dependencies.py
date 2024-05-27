from repositories.users import StudentRepository
from services.users import StudentService


def student_service():
    return StudentService(StudentRepository)
