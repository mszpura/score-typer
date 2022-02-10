from datetime import datetime
from typing import List, Optional, Text
from uuid import uuid4, UUID
from pydantic import BaseModel

from .abstract_entity import AbstractEntity


class Team(BaseModel):
    name: Text
    score: Optional[int]
    scored_players: List[int]

    @classmethod
    def create(cls, team_name: Text) -> "Team":
        return cls(name=team_name, scored_players=[])

    def update_result(self,
                      score: int,
                      scored_players: List[int]):
        self.score = score
        self.scored_players = scored_players

    def update(self, team_name: Text) -> None:
        self.name = team_name


class Game(AbstractEntity):
    id: UUID
    tournament_id: UUID
    finished_date: Optional[datetime]
    home: Team
    away: Team

    @classmethod
    def create(cls,
               tournament_id: UUID,
               home_team_name: Text,
               away_team_name: Text) -> "Game":
        home = Team.create(home_team_name)
        away = Team.create(away_team_name)
        return cls(id=str(uuid4()), tournament_id=tournament_id, home=home, away=away, finished_date=None)

    def update(self,
               tournament_id: UUID,
               home_team_name: Text,
               away_team_name: Text) -> None:
        self.tournament_id = tournament_id
        self.home.update(home_team_name)
        self.away.update(away_team_name)

    def finish(self,
               finished_date: datetime,
               home_score: int,
               away_score: int,
               scored_home_players: List[int],
               scored_away_players: List[int]):
        self.finished_date = finished_date
        self.home.update_result(home_score, scored_home_players)
        self.away.update_result(away_score, scored_away_players)
