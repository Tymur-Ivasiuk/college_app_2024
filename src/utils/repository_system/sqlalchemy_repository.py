from sqlalchemy import insert, select, literal_column

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

    async def find_all(self) -> list:
        async with async_session_maker() as session:
            query = select(self.model)
            res = await session.execute(query)
            res = [row[0].to_read_model() for row in res.all()]
            return res


