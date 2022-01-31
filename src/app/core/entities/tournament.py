from typing import Text, Optional
from datetime import datetime
from uuid import  uuid4
from pydantic import BaseModel


class Tournament(BaseModel):
    id: Text
    name: Text
    description: Optional[Text]
    last_date_to_register: datetime

    @classmethod
    def create(cls, **kwargs) -> "Tournament":
        return Tournament(id=uuid4(), **kwargs)

    def update(self, name: Text, desc: Text, last_date_to_register: datetime) -> None:
        if name:
            self.name = name
        if desc:
            self.description = desc
        if last_date_to_register:
            self.last_date_to_register = last_date_to_register
