from dataclasses import dataclass
from datetime import datetime


@dataclass
class Tournament:
    id: int
    name: str
    description: str
    last_register_date: datetime
