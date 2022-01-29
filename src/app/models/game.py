from dataclasses import dataclass
from typing import List, Optional
from uuid import UUID

from .tournament import Tournament


@dataclass
class TeamResult:
    score: int
    is_winner: bool
    scored_players: List[int]


@dataclass
class Game:
    id: UUID
    tournament: Tournament
    is_finished: bool
    home_result: Optional[TeamResult]
    away_result: Optional[TeamResult]
