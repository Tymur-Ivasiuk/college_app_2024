from utils import AbstractRepository
from schemas.users.role import RoleCreateDTO


# Maybe write abstraction or superClass for role management and all other models
class RoleService:
    def __init__(self, role_repo: type[AbstractRepository]):
        self.role_repo: AbstractRepository = role_repo()

    async def add_role(self, role: RoleCreateDTO):
        role_dict = role.model_dump()
        role_id = await self.role_repo.add_one(role_dict)
        return role_id

    async def find_all(self):
        roles = await self.role_repo.find_all()
        return roles
