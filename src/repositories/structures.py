from utils.repository_system import SQLAlchemyRepository
from models.structures import *


class DepartmentRepository(SQLAlchemyRepository):
    model = Department


class SpecialtyRepository(SQLAlchemyRepository):
    model = Specialty
