from app.api.dtos.user_dto import UserDto


async def post(payload: UserDto):
    # query = users.insert().values(username=payload.username, password=payload.password, email=payload.email)
    # return await database.execute(query=query)
    pass


async def get(user_id: int):
    # query = users.select().where(users.c.id == user_id)
    # return await database.fetch_one(query=query)
    pass


async def get_all():
    # query = users.select()
    # return await database.fetch_all(query)
    pass


async def put(user_id: int, payload: UserDto):
    # query = (
    #     users
    #     .update()
    #     .where(users.c.id == user_id)
    #     .values(username=payload.username, password=payload.password, email=payload.email)
    #     .returning(users.c.id)
    # )
    # return await database.execute(query)
    pass


async def delete(user_id: int):
    # query = users.delete().where(users.c.id == user_id)
    # return await database.execute(query)
    pass