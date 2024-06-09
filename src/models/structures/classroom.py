from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base, intpk, str50
from models.structures.building import Building


class Classroom(Base):
    __tablename__ = 'classroom'

    id: Mapped[intpk]

    title: Mapped[str50]
    max_student_capacity: Mapped[int]
    features: Mapped[str] = mapped_column(nullable=True)

    building_id: Mapped[int] = mapped_column(ForeignKey('building.id', ondelete='CASCADE'))
    building: Mapped[Building] = relationship(Building)
