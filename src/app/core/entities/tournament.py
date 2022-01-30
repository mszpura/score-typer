from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class Tournament:
    id: UUID
    name: str
    description: str
    last_register_date: datetime
