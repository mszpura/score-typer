from fastapi import FastAPI
from app.api.routes import users_route

app = FastAPI()


# @app.on_event("startup")
# async def startup():
#     await engine.begin()
#
#
# @app.on_event("shutdown")
# async def shutdown():
#     await engine.dispose()


app.include_router(users_route.router, prefix="/users", tags=["users"])
