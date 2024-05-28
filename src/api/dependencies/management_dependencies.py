from repositories.users import StudentRepository, TeacherRepository
from services.users import StudentService, TeacherService


def student_service():
    return StudentService(StudentRepository)


def teacher_service():
    return TeacherService(TeacherRepository)
