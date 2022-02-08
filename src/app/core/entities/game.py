from datetime import datetime
from typing import List, Optional
from uuid import uuid4
from pydantic import BaseModel

from .abstract_entity import AbstractEntity
from .tournament import Tournament


class TeamResult(BaseModel):
    score: int
    is_winner: bool
    scored_players: List[int]


class Game(AbstractEntity):
    tournament: Tournament
    finished_date: datetime
    home_result: Optional[TeamResult]
    away_result: Optional[TeamResult]

    @classmethod
    def create(cls, **kwargs) -> "Game":
        return cls(id=str(uuid4()), **kwargs)

    def update(self, **kwargs):
        pass
