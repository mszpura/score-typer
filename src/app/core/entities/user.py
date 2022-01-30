from dataclasses import dataclass
from uuid import UUID


@dataclass
class User:
    id: str
    username: str
    password: str
    email: str
