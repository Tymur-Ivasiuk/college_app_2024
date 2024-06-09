from repositories.structures import (
    DepartmentRepository,
    SpecialtyRepository,
    GroupRepository,
    BuildingRepository,
    ClassroomRepository,
)

from services.structures import (
    DepartmentService,
    SpecialtyService,
    GroupService,
    BuildingService,
    ClassroomService,
)


def department_service():
    return DepartmentService(DepartmentRepository)


def specialty_service():
    return SpecialtyService(SpecialtyRepository)


def group_service():
    return GroupService(GroupRepository)


def building_service():
    return BuildingService(BuildingRepository)


def classroom_service():
    return ClassroomService(ClassroomRepository)
