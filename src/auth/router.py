from auth.config import fastapi_users, auth_backend
from auth.schemas import UserReadDTO, UserCreateDTO


auth_router = fastapi_users.get_auth_router(
    auth_backend
)

register_router = fastapi_users.get_register_router(
    user_schema=UserReadDTO,
    user_create_schema=UserCreateDTO,
)

