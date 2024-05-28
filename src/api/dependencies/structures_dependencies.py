from repositories.structures import DepartmentRepository
from services.structures import DepartmentService

from repositories.structures import SpecialtyRepository
from services.structures import SpecialtyService

from repositories.structures import GroupRepository
from services.structures import GroupService


def department_service():
    return DepartmentService(DepartmentRepository)


def specialty_service():
    return SpecialtyService(SpecialtyRepository)


def group_service():
    return GroupService(GroupRepository)
