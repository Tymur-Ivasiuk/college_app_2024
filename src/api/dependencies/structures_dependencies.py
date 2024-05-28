from repositories.structures import DepartmentRepository
from services.structures import DepartmentService


def department_service():
    return DepartmentService(DepartmentRepository)
