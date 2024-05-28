from typing import List, Annotated

from fastapi import APIRouter, Depends

from schemas.structures.specialty import SpecialtyReadDTO, SpecialtyCreateDTO
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


@specialty_router.post("", response_model=SpecialtyReadDTO)
async def add_specialty(
    specialty_data: SpecialtyCreateDTO,
    specialty_service: Annotated[SpecialtyService, Depends(specialty_service)]
):
    specialty = await specialty_service.add_one(specialty_data)
    return specialty
