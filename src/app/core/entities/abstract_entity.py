from abc import ABC, abstractmethod

from pydantic import BaseModel


class AbstractEntity(ABC, BaseModel):
    id: str

    @classmethod
    @abstractmethod
    def create(cls, **kwargs):
        raise NotImplementedError
