from fastapi import FastAPI

from app.api.composition.tournaments_module import add_tournaments_routing
from app.api.composition.users_module import add_users_routing

app = FastAPI()

add_users_routing(app, "users")
add_tournaments_routing(app, "tournaments")
