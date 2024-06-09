from typing import List, Annotated

from fastapi import APIRouter, Depends

from api.dependencies.learning_proccess_dependencies import grade_event_service
from services.learning_proccess import GradeEventService
from schemas.learning_proccess.grade_event import GradeEventReadDTO, GradeEventCreateDTO, GradeEventUpdateDTO

grade_event_router = APIRouter(
    prefix="/grade_events",
    tags=["GradeEvents"],
)


@grade_event_router.get("", response_model=List[GradeEventReadDTO])
async def get_grade_events(grade_event_service: Annotated[GradeEventService, Depends(grade_event_service)]):
    grade_events = await grade_event_service.find_all()
    return grade_events


@grade_event_router.get('/{rec_id}', response_model=GradeEventReadDTO)
async def get_grade_event(rec_id: int, grade_event_service: Annotated[GradeEventService, Depends(grade_event_service)]):
    grade_events = await grade_event_service.get_one(rec_id)
    return grade_events


@grade_event_router.post("", response_model=GradeEventReadDTO)
async def add_grade_event(
    grade_event: GradeEventCreateDTO,
    grade_event_service: Annotated[GradeEventService, Depends(grade_event_service)]
):
    grade_event = await grade_event_service.add_one(grade_event)
    return grade_event


@grade_event_router.put("/{rec_id}", response_model=GradeEventReadDTO)
async def update_grade_event(
    rec_id: int,
    grade_event: GradeEventUpdateDTO,
    grade_event_service: Annotated[GradeEventService, Depends(grade_event_service)]
):
    grade_event = await grade_event_service.update_by_id(rec_id, grade_event)
    return grade_event


@grade_event_router.delete("/{rec_id}", response_model=bool)
async def delete_grade_event(
    rec_id: int,
    grade_event_service: Annotated[GradeEventService, Depends(grade_event_service)]
):
    return await grade_event_service.delete_by_id(rec_id)
