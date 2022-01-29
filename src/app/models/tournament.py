from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class Tournament:
    id: UUID
    name: str
    last_register_date: datetime