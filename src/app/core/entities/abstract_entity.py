from abc import ABC, abstractmethod
from typing import Text

from pydantic import BaseModel


class AbstractDto(ABC, BaseModel):
    pass


class AbstractEntity(ABC, BaseModel):
    id: Text

    @classmethod
    @abstractmethod
    def create(cls, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def update(self, **kwargs):
        raise NotImplementedError
