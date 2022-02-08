from datetime import datetime
from typing import Text, Optional

from app.core.entities.abstract_entity import AbstractDto


class TournamentDto(AbstractDto):
    name: Text
    description: Optional[Text]
    last_date_to_register: datetime
    finished_date: Optional[datetime]
