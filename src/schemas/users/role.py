from pydantic import BaseModel


class RoleCreateDTO(BaseModel):
    title: str
    permissions: dict | None


class RoleReadDTO(RoleCreateDTO):
    id: int
