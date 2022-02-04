from fastapi import FastAPI, Depends

from app.api.composition_root import compose_tournaments_repository
from app.api.dtos.tournament_dto import TournamentDto
from app.api.routes import users_route
from app.api.routes.crud_route_factory import create_crud_router_for
from app.core.entities.tournament import Tournament

app = FastAPI()


app.include_router(users_route.router, prefix="/users", tags=["user"])

tournaments_routes = create_crud_router_for(Tournament, compose_tournaments_repository, TournamentDto)
app.include_router(tournaments_routes, prefix="/tournaments", tags=["tournament"])
