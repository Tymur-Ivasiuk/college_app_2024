from utils import SQLAlchemyRepository
from models import BaseUser, Role


class UserRepository(SQLAlchemyRepository):
    model = BaseUser
    

class RoleRepository(SQLAlchemyRepository):
    model = Role
