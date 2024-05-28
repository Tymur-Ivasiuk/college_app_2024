from services.users.role import RoleService
from repositories.users import RoleRepository


def role_service():
    return RoleService(RoleRepository)
