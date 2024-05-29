from utils.repository_system import AbstractRepository
from schemas.structures.group import GroupCreateDTO, GroupReadRelDTO


class GroupService:
    def __init__(self, group_repo: type[AbstractRepository]):
        self.group_repo: AbstractRepository = group_repo()

    async def find_all(self):
        groups = await self.group_repo.find_all(
            selectin_field_names=['curator', 'specialty'],
            to_read_model=False
        )

        groups_data = [
            GroupReadRelDTO.model_validate(group).model_dump()
            for group in groups
        ]

        return groups_data

    async def add_one(self, group_data: GroupCreateDTO):
        group_dict = group_data.model_dump()
        group = await self.group_repo.add_one(group_dict)
        return group
