from fastapi import APIRouter

router = APIRouter()


@router.put(f"/game/{id}/finish")
def finish_game_handler():
    pass
