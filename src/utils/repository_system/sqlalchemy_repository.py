from sqlalchemy import insert, select, literal_column
from sqlalchemy.orm import selectinload, joinedload

from utils.repository_system import AbstractRepository
from db.database import async_session_maker


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict) -> dict:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one().to_read_model()

    async def find_all(self, selectin_field_names: list = [], to_read_model: bool = True) -> list:
        async with async_session_maker() as session:
            query = select(self.model)

            if selectin_field_names:
                query = query.options(
                    *[
                        joinedload(getattr(self.model, selectin_field))
                        for selectin_field in selectin_field_names
                    ]
                )

            res = await session.execute(query)
            rows = res.scalars().all()

            if to_read_model:
                rows = [row.to_read_model() for row in rows]

            return rows
