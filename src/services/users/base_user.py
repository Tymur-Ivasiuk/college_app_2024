from utils import AbstractRepository
from schemas.users import BaseUserCreateDTO


class BaseUserService:
    def __init__(self, base_user_repo: type[AbstractRepository]):
        self.base_user_repo: AbstractRepository = base_user_repo()

    async def add_user(self, user: BaseUserCreateDTO):
        user_dict = user.model_dump()
        user_id = await self.base_user_repo.add_one(user_dict)
        return user_id

