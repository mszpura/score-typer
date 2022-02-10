from typing import Text
from uuid import UUID

from app.core.entities.abstract_entity import AbstractDto


class GameDto(AbstractDto):
    tournament_id: UUID
    home_team_name: Text
    away_team_name: Text
