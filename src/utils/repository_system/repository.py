from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict) -> int:
        raise NotImplemented

    @abstractmethod
    async def find_all(self):
        raise NotImplemented




