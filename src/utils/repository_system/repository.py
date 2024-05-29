from abc import ABC, abstractmethod
from typing import Optional


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(
            self,
            data: dict,
            to_read_model: bool,
            selectin_field_names: list
    ) -> dict:
        raise NotImplemented

    @abstractmethod
    async def find_all(
        self,
        to_read_model: bool,
        filters_list: dict,
        selectin_field_names: list,
        limit: int,
    ) -> list:
        raise NotImplemented

    async def get_one(
        self,
        rec_id: int,
        to_read_model: bool = True,
        selectin_field_names: list = [],
    ) -> dict:
        raise NotImplemented
