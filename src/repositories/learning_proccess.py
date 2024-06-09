from utils import SQLAlchemyRepository
from models.learning_proccess import *


class GradeRepository(SQLAlchemyRepository):
    model = Grade


class GradeEventRepository(SQLAlchemyRepository):
    model = GradeEvent


class LectureRepository(SQLAlchemyRepository):
    model = Lecture


class LecturePeriodRepository(SQLAlchemyRepository):
    model = LecturePeriod


class SubjectRepository(SQLAlchemyRepository):
    model = Subject
