from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict) -> int:
        raise NotImplemented

    @abstractmethod
    async def find_all(self, selectin_field_names: list, to_read_model: bool) -> list:
        raise NotImplemented




