from typing import List, Annotated

from fastapi import APIRouter, Depends

from api.dependencies.structures_dependencies import classroom_service
from services.structures import ClassroomService
from schemas.structures.classroom import ClassroomReadDTO, ClassroomCreateDTO, ClassroomUpdateDTO

classroom_router = APIRouter(
    prefix="/classrooms",
    tags=["Classrooms"],
)


@classroom_router.get("", response_model=List[ClassroomReadDTO])
async def get_classrooms(classroom_service: Annotated[ClassroomService, Depends(classroom_service)]):
    classrooms = await classroom_service.find_all()
    return classrooms


@classroom_router.get('/{rec_id}', response_model=ClassroomReadDTO)
async def get_classroom(rec_id: int, classroom_service: Annotated[ClassroomService, Depends(classroom_service)]):
    classrooms = await classroom_service.get_one(rec_id)
    return classrooms


@classroom_router.post("", response_model=ClassroomReadDTO)
async def add_classroom(
    classroom: ClassroomCreateDTO,
    classroom_service: Annotated[ClassroomService, Depends(classroom_service)]
):
    classroom = await classroom_service.add_one(classroom)
    return classroom


@classroom_router.put("/{rec_id}", response_model=ClassroomReadDTO)
async def update_classroom(
    rec_id: int,
    classroom: ClassroomUpdateDTO,
    classroom_service: Annotated[ClassroomService, Depends(classroom_service)]
):
    classroom = await classroom_service.update_by_id(rec_id, classroom)
    return classroom


@classroom_router.delete("/{rec_id}", response_model=bool)
async def delete_classroom(
    rec_id: int,
    classroom_service: Annotated[ClassroomService, Depends(classroom_service)]
):
    return await classroom_service.delete_by_id(rec_id)
