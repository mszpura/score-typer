from abc import ABC, abstractmethod
from typing import Text

from pydantic import BaseModel


class AbstractEntity(ABC, BaseModel):
    id: Text

    @classmethod
    @abstractmethod
    def create(cls, **kwargs):
        raise NotImplementedError
