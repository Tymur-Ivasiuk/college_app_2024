from utils import SQLAlchemyRepository
from models.learning_proccess import *


class GroupRepository(SQLAlchemyRepository):
    model = Group
