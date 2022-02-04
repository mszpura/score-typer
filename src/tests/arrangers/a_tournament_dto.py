from datetime import datetime
from uuid import uuid4


class ATournamentDto:
    def build(self):
        return TournamentDto(
            name=f"{uuid4()}",
            description=f"{uuid4()}",
            last_date_to_register=datetime.now(),
            finished_date=None
        )
    