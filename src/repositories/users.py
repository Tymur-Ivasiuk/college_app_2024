from utils import SQLAlchemyRepository
from models.users import *


class UserRepository(SQLAlchemyRepository):
    model = BaseUser


class TeacherRepository(SQLAlchemyRepository):
    model = Teacher


class StudentRepository(SQLAlchemyRepository):
    model = Student


class RoleRepository(SQLAlchemyRepository):
    model = Role
