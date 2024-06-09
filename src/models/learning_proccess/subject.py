from sqlalchemy.orm import Mapped, mapped_column
from db import Base, intpk


class Subject(Base):
    __tablename__ = 'subject'

    id: Mapped[intpk]

    title: Mapped[str]
    is_professional: Mapped[bool] = mapped_column(default=True)

