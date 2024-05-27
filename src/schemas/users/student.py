from .base_user import BaseUserReadDTO, BaseUserCreateDTO
from ..learning_proccess.group import GroupReadDTO


class StudentCreateDTO(BaseUserCreateDTO):
    """
    - User creation (if user_id == None)
    - Student creation
    """
    user_id: int = None
    group_id: int


class StudentReadDTO(BaseUserReadDTO):
    id: int
    group_id: "GroupReadDTO"


StudentReadDTO.update_forward_refs()
