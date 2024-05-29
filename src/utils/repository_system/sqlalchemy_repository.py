from sqlalchemy import insert, select, literal_column, and_
from sqlalchemy.orm import selectinload, joinedload

from utils.repository_system import AbstractRepository
from db.database import async_session_maker


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(
            self,
            data: dict,
            to_read_model: bool = True,
            selectin_field_names: list = [],
    ) -> dict:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            new_id = res.scalar_one()
            await session.commit()

            created_row = await self.get_one(
                rec_id=new_id,
                selectin_field_names=selectin_field_names,
                to_read_model=to_read_model,
            )
            return created_row

    async def find_all(
            self,
            to_read_model: bool = True,
            filters_list: list = [],
            selectin_field_names: list = [],
            limit: int = 100,
    ) -> list:
        async with async_session_maker() as session:
            query = select(self.model).limit(limit)

            query = self.__get_filters_query(query=query, filters_list=filters_list)
            query = self.__get_loaded_query(query=query, selectin_field_names=selectin_field_names)

            res = await session.execute(query)
            rows = res.scalars().all()

            if to_read_model:
                rows = [row.to_read_model() for row in rows]

            return rows

    async def get_one(
            self,
            rec_id: int,
            to_read_model: bool = True,
            selectin_field_names: list = [],
    ) -> dict:
        filters_list = [
            ("id", "==", rec_id),
        ]
        row = await self.find_all(
            to_read_model=to_read_model,
            filters_list=filters_list,
            selectin_field_names=selectin_field_names,
            limit=1,
        )
        return row[0] if row else {}

    def __get_filters_query(self, query, filters_list: list):
        """
        :param query: default query
        :param filters_list:
            example: [
                ('first_name', '==', 'John'),
                ('email', 'like', '%@example.com')
            ]
        :return: query
        """
        if filters_list:
            filter_conditions = []
            for filter_item in filters_list:
                field_name, operator, value = filter_item
                field = getattr(self.model, field_name)
                condition = None
                if operator == '==':
                    condition = (field == value)
                elif operator == '!=':
                    condition = (field != value)
                elif operator == '>':
                    condition = (field > value)
                elif operator == '<':
                    condition = (field < value)
                elif operator == '>=':
                    condition = (field >= value)
                elif operator == '<=':
                    condition = (field <= value)
                elif operator == 'in':
                    condition = field.in_(value)
                elif operator == 'like':
                    condition = field.like(value)

                if condition is not None:
                    filter_conditions.append(condition)
            query = query.filter(and_(*filter_conditions))

        return query

    def __get_loaded_query(self, query, selectin_field_names: list):
        if selectin_field_names:
            query = query.options(
                *[
                    joinedload(getattr(self.model, selectin_field))
                    for selectin_field in selectin_field_names
                ]
            )
        return query
