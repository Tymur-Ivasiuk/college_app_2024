from core.auth_config import auth_backend, fastapi_users
from schemas.users.base_user import BaseUserReadDTO, BaseUserCreateDTO

auth_router = fastapi_users.get_auth_router(
    auth_backend
)

register_router = fastapi_users.get_register_router(
    user_schema=BaseUserReadDTO,
    user_create_schema=BaseUserCreateDTO,
)
