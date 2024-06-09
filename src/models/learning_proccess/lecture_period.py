from sqlalchemy import TIME
from sqlalchemy.orm import Mapped, mapped_column
from db import Base, intpk, str50


class LecturePeriod(Base):
    __tablename__ = 'lecture_period'

    id: Mapped[intpk]

    title: Mapped[str50]
    start_at: Mapped[TIME] = mapped_column(TIME)
    end_at: Mapped[TIME] = mapped_column(TIME)
