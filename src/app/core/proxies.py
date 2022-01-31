from abc import ABC, abstractmethod
from uuid import UUID


class AbstractRepository(ABC):

    @abstractmethod
    def create(self, entity):
        raise NotImplementedError

    @abstractmethod
    def get(self, id: UUID):
        raise NotImplementedError

    @abstractmethod
    def get_all(self):
        raise NotImplementedError

    @abstractmethod
    def update(self, entity):
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: UUID):
        raise NotImplementedError
