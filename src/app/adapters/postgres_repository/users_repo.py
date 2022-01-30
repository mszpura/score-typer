import json
import uuid
from app.core.entities.user import User
from sqlalchemy.orm import Session
from datetime import datetime


class UsersRepository:
    TABLE_NAME = "users"

    def __init__(self, session: Session):
        self.session = session

    async def create(self, user: User):
        user_json = json.dumps(user.__dict__)
        await self.session.execute(
            f"INSERT INTO {self.TABLE_NAME} (id, json, created_date) VALUES (:id, :json, :created_date)",
            {"id":  uuid.UUID(user.id), "json": user_json, "created_date": datetime.now()})

    async def update(self, id: int, item):
        pass

    async def delete(self, id: int):
        pass

    async def get(self, id: uuid.UUID):
        result = await self.session.execute(
            f"SELECT Json FROM {self.TABLE_NAME} WHERE id = :id",
            {"id": str(id)})
        row = result.fetchone()


    async def get_all(self):
        pass
