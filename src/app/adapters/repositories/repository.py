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
        entity = result.fetchone()
        if entity:
            return self.map_entity(entity)
        return None

    async def get_all(self) -> List[AbstractEntity]:
        result = await self.session.execute(f"SELECT * FROM {self.table_name}")
        return list(map(self.map_entity, result.fetchall()))

    async def update(self, entity: AbstractEntity) -> None:
        await self.session.execute(
            f"UPDATE {self.table_name} SET json = :json WHERE id = :id",
            {"json": entity.json(), "id": UUID(entity.id)})
        await self.session.commit()

    async def delete(self, id: UUID):
        await self.session.execute(f"DELETE FROM {self.table_name} WHERE id = :id", {"id": id})
        await self.session.commit()

    def map_entity(self, entity):
        return self.entity_type(**entity["json"])
