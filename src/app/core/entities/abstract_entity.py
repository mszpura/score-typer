from abc import ABC, abstractmethod
from uuid import UUID

from pydantic import BaseModel


class AbstractDto(ABC, BaseModel):
    pass


class AbstractEntity(ABC, BaseModel):
    id: UUID

    @classmethod
    @abstractmethod
    def create(cls, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def update(self, **kwargs):
        raise NotImplementedError

    # Necessary configuration in domain because apparently Pydantic cannot parse UUID into json :/
    class Config:
        json_encoders = {
            UUID: lambda i: str(i)
        }
