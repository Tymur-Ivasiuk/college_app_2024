from .base_user import BaseUserReadDTO, BaseUserCreateDTO
from ..structures.department import DepartmentReadDTO


class TeacherCreateDTO(BaseUserCreateDTO):
    """
    - User creation (if user_id == None)
    - Teacher creation
    """
    user_id: int = None
    department_id: int


class TeacherReadDTO(BaseUserReadDTO):
    id: int
    department_id: "DepartmentReadDTO"


TeacherReadDTO.update_forward_refs()