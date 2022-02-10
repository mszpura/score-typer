from uuid import uuid4

from app.api.dtos.game_dto import GameDto


class AGameDto:
    def build(self):
        return GameDto(
            tournament_id=uuid4(),
            home_team_name=f"{uuid4()}",
            away_team_name=f"{uuid4()}"
        )
