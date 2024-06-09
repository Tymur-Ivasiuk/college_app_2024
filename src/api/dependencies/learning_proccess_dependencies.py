from repositories.learning_proccess import (
    GradeRepository,
    GradeEventRepository,
    LectureRepository,
    LecturePeriodRepository,
    SubjectRepository
)
from services.learning_proccess.grade import GradeService
from services.learning_proccess.grade_event import GradeEventService
from services.learning_proccess.lecture import LectureService
from services.learning_proccess.lecture_period import LecturePeriodService
from services.learning_proccess.subject import SubjectService


def grade_service():
    return GradeService(GradeRepository)


def grade_event_service():
    return GradeEventService(GradeEventRepository)


def lecture_service():
    return LectureService(LectureRepository)


def lecture_period_service():
    return LecturePeriodService(LecturePeriodRepository)


def subject_service():
    return SubjectService(SubjectRepository)

