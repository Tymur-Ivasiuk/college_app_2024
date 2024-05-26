from typing import Optional

from fastapi import Request, Depends
from fastapi_users import BaseUserManager, IntegerIDMixin

from models.users import BaseUser


class UserManager(IntegerIDMixin, BaseUserManager[BaseUser, int]):
    async def on_after_register(self, user: BaseUser, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")
