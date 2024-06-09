from sqlalchemy.orm import Mapped, mapped_column
from db import Base, intpk


class Building(Base):
    __tablename__ = 'building'

    id: Mapped[intpk]
    title: Mapped[str]
    address: Mapped[str]

    lat: Mapped[float]
    lng: Mapped[float]

    # TODO: add rel for classroooms

