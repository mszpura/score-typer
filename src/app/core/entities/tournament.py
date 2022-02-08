from typing import Text, Optional
from datetime import datetime
from uuid import uuid4

from .abstract_entity import AbstractEntity


class Tournament(AbstractEntity):
    name: Text
    description: Optional[Text]
    last_date_to_register: datetime
    finished_date: Optional[datetime]

    @classmethod
    def create(cls, **kwargs) -> "Tournament":
        return cls(id=str(uuid4()), **kwargs)

    def update(self,
               name: Text,
               description: Optional[Text],
               last_date_to_register: datetime,
               finished_date: Optional[datetime]) -> None:
        self.name = name
        self.description = description
        self.last_date_to_register = last_date_to_register
        self.finished_date = finished_date
