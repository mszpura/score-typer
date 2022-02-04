from datetime import datetime
from typing import Text, Optional

from app.api.dtos.abstract_dto import AbstractDto


class TournamentDto(AbstractDto):
    name: Text
    description: Optional[Text]
    last_date_to_register: datetime
    #finished_date: Optional[datetime]
