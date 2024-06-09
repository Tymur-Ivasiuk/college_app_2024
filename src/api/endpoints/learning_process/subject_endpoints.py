from typing import List, Annotated

from fastapi import APIRouter, Depends

from api.dependencies.learning_proccess_dependencies import subject_service
from services.learning_proccess import SubjectService
from schemas.learning_proccess.subject import SubjectReadDTO, SubjectCreateDTO, SubjectUpdateDTO

subject_router = APIRouter(
    prefix="/subjects",
    tags=["Subjects"],
)


@subject_router.get("", response_model=List[SubjectReadDTO])
async def get_subjects(subject_service: Annotated[SubjectService, Depends(subject_service)]):
    subjects = await subject_service.find_all()
    return subjects


@subject_router.get('/{rec_id}', response_model=SubjectReadDTO)
async def get_subject(rec_id: int, subject_service: Annotated[SubjectService, Depends(subject_service)]):
    subjects = await subject_service.get_one(rec_id)
    return subjects


@subject_router.post("", response_model=SubjectReadDTO)
async def add_subject(
    subject: SubjectCreateDTO,
    subject_service: Annotated[SubjectService, Depends(subject_service)]
):
    subject = await subject_service.add_one(subject)
    return subject


@subject_router.put("/{rec_id}", response_model=SubjectReadDTO)
async def update_subject(
    rec_id: int,
    subject: SubjectUpdateDTO,
    subject_service: Annotated[SubjectService, Depends(subject_service)]
):
    subject = await subject_service.update_by_id(rec_id, subject)
    return subject


@subject_router.delete("/{rec_id}", response_model=bool)
async def delete_subject(
    rec_id: int,
    subject_service: Annotated[SubjectService, Depends(subject_service)]
):
    return await subject_service.delete_by_id(rec_id)
