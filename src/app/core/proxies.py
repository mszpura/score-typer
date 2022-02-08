from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from app.core.entities.abstract_entity import AbstractEntity


class AbstractRepository(ABC):

    @abstractmethod
    async def create(self, entity) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get(self, id: UUID) -> AbstractEntity:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self) -> List[AbstractEntity]:
        raise NotImplementedError

    @abstractmethod
    async def update(self, entity) -> None:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, id: UUID) -> None:
        raise NotImplementedError
