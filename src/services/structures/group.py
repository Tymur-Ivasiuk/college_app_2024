from fastapi import HTTPException

from utils.repository_system import AbstractRepository
from schemas.structures.group import GroupCreateDTO, GroupReadRelDTO, GroupUpdateDTO


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
    
    async def get_one(self, rec_id):
        group = await self.group_repo.get_one(
            rec_id=rec_id,
            to_read_model=False,
            selectin_field_names=['curator', 'specialty'],
        )
        return group

    async def add_one(self, group_data: GroupCreateDTO):
        group_dict = group_data.model_dump()
        group = await self.group_repo.add_one(group_dict)
        return group

    async def update_by_id(self, rec_id: int, group: GroupUpdateDTO):
        group_dict = group.model_dump(exclude_unset=True)

        update_group_status = await self.group_repo.update_by_id(
            rec_id,
            group_dict,
        )
        if not update_group_status:
            raise HTTPException(status_code=404, detail={
                "info": "No record to update"
            })

        group = await self.get_one(rec_id=rec_id)
        return group

    async def delete_by_id(self, rec_id: int):
        return await self.group_repo.delete_by_id(rec_id)