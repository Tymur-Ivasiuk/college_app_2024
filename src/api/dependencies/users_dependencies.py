from services.users.role import RoleService
from repositories.users import RoleRepository

from repositories.users import StudentRepository, TeacherRepository, UserRepository
from services.users import StudentService, TeacherService


def role_service():
    return RoleService(RoleRepository)


def student_service():
    return StudentService(StudentRepository, UserRepository)


def teacher_service():
    return TeacherService(TeacherRepository)
