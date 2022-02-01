from typing import Text, List, Type
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.entities.abstract_entity import AbstractEntity
from app.core.proxies import AbstractRepository


class Repository(AbstractRepository):
    def __init__(self, table_name: Text, entity_type: Type[AbstractEntity], session: AsyncSession):
        self.table_name = table_name
        self.session = session
        self.entity_type = entity_type

    async def create(self, user: AbstractEntity) -> None:
        await self.session.execute(
            f"INSERT INTO {self.table_name} (id, json) VALUES (:id, :json)",
            {"id": UUID(user.id), "json": user.json()})
        await self.session.commit()

    async def get(self, id: UUID) -> AbstractEntity | None:
        result = await self.session.execute(
            f"SELECT json FROM {self.table_name} WHERE id = :id",
            {"id": str(id)})
        user = result.fetchone()
        if user is not None:
            return self.map_user(user)
        return None

    async def get_all(self) -> List[AbstractEntity]:
        result = await self.session.execute(f"SELECT * FROM {self.table_name}")
        return list(map(self.map_user, result.fetchall()))

    async def update(self, user: AbstractEntity) -> None:
        await self.session.execute(
            f"UPDATE {self.table_name} SET json = :json WHERE id = :id",
            {"json": user.json(), "id": UUID(user.id)})
        await self.session.commit()

    async def delete(self, user_id: UUID):
        await self.session.execute(f"DELETE FROM {self.table_name} WHERE id = :id", {"id": user_id})
        await self.session.commit()

    def map_user(self, user):
        return self.entity_type.create(**user["json"])
