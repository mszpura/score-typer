from abc import ABC, abstractmethod
from typing import Text

from pydantic import BaseModel


class AbstractDto(ABC, BaseModel):
    pass


class AbstractEntity(ABC):
    id: Text
    dto: AbstractDto

    @classmethod
    @abstractmethod
    def create(cls, **kwargs):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def update(cls, **kwargs):
        raise NotImplementedError
