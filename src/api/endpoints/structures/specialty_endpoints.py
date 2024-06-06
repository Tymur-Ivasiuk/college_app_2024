from typing import List, Annotated

from fastapi import APIRouter, Depends

from schemas.structures.specialty import SpecialtyReadDTO, SpecialtyCreateDTO, SpecialtyUpdateDTO
from api.dependencies.structures_dependencies import specialty_service
from services.structures import SpecialtyService


specialty_router = APIRouter(
    prefix="/specialties",
    tags=["Specialties"],
)


@specialty_router.get("", response_model=List[SpecialtyReadDTO])
async def get_specialties(specialty_service: Annotated[SpecialtyService, Depends(specialty_service)]):
    specialties = await specialty_service.find_all()
    return specialties


@specialty_router.get('/{rec_id}', response_model=SpecialtyReadDTO)
async def get_specialty(rec_id: int, specialty_service: Annotated[SpecialtyService, Depends(specialty_service)]):
    specialtys = await specialty_service.get_one(rec_id)
    return specialtys


@specialty_router.post("", response_model=SpecialtyReadDTO)
async def add_specialty(
    specialty_data: SpecialtyCreateDTO,
    specialty_service: Annotated[SpecialtyService, Depends(specialty_service)]
):
    specialty = await specialty_service.add_one(specialty_data)
    return specialty


@specialty_router.put("/{rec_id}", response_model=SpecialtyReadDTO)
async def update_specialty(
    rec_id: int,
    specialty: SpecialtyUpdateDTO,
    specialty_service: Annotated[SpecialtyService, Depends(specialty_service)]
):
    specialty = await specialty_service.update_by_id(rec_id, specialty)
    return specialty


@specialty_router.delete("/{rec_id}", response_model=bool)
async def delete_specialty(
    rec_id: int,
    specialty_service: Annotated[SpecialtyService, Depends(specialty_service)]
):
    return await specialty_service.delete_by_id(rec_id)

