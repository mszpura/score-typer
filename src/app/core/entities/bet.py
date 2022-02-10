from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel

from .abstract_entity import AbstractEntity
from ..exceptions import NotSelectedScorerError

points_per_win = 1
points_per_exact_score = 3
points_per_typed_scored_player = 2


class TeamBet(BaseModel):
    score: int
    is_winner: bool
    scored_player: Optional[int]

    @classmethod
    def create(cls, score: int, is_winner: bool, scored_player: Optional[int]) -> "TeamBet":
        return cls(score=score, scored_player=scored_player, is_winner=is_winner)

    def update(self, score: int, is_winner: bool, scored_player: Optional[int]) -> None:
        self.score = score
        self.is_winner = is_winner
        self.scored_player = scored_player


class Bet(AbstractEntity):
    id: UUID
    game_id: UUID
    owner_id: UUID
    home_bet: TeamBet
    away_bet: TeamBet
    points_earned: Optional[int]

    @classmethod
    def create(cls,
               game_id: UUID,
               owner_id: UUID,
               home_score: int,
               away_score: int,
               is_home_wins: bool,
               is_away_wins: bool,
               home_scorer: Optional[int],
               away_scorer: Optional[int]) -> "Bet":

        if home_scorer is None and away_scorer is None:
            raise NotSelectedScorerError(f"No scorer has been selected")

        home_bet = TeamBet.create(home_score, is_home_wins, home_scorer)
        away_bet = TeamBet.create(away_score, is_away_wins, away_scorer)
        return Bet(id=uuid4(), game_id=game_id, owner_id=owner_id, home_bet=home_bet, away_bet=away_bet)

    def update(self,
               game_id: UUID,
               owner_id: UUID,
               home_score: int,
               away_score: int,
               is_home_wins: bool,
               is_away_wins: bool,
               home_scorer: Optional[int],
               away_scorer: Optional[int]):
        self.game_id = game_id
        self.owner_id = owner_id
        self.home_bet.update(home_score, is_home_wins, home_scorer)
        self.away_bet.update(away_score, is_away_wins, away_scorer)

    def add_points(self, scored: int):
        self.points_earned = scored
