from dataclasses import dataclass
from uuid import UUID


@dataclass
class User:
    id: UUID
    username: str
    password: str
    email: str
