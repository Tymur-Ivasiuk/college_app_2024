from fastapi_users import schemas, models
from pydantic import EmailStr


class UserReadDTO(schemas.BaseUser[int]):
    id: models.ID

    first_name: str
    last_name: str
    patronymic: str

    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserCreateDTO(schemas.BaseUserCreate):
    first_name: str
    last_name: str
    patronymic: str

    email: EmailStr
    password: str

    is_active: bool | None = True
    is_superuser: bool | None = False
    is_verified: bool | None = False
