from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException, Path

from app.api.handlers import user_handlers
from app.api.dtos.user_dto import UserDto
from app.core.entities.user import User

router = APIRouter()


@router.post("", response_model=User, status_code=201)
async def create_user(payload: UserDto):
    return await user_handlers.create(payload)


@router.get("/{user_id}", response_model=User)
async def get_user(user_id: UUID = Path(..., gt=0)):
    user = await user_handlers.get_by(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
#
#
# @router.get("", response_model=List[User])
# async def get_all():
#     # return await crud.get_all()
#     pass
#
#
# @router.put("/{user_id}", response_model=User)
# async def update_user(payload: UserDto, user_id: int = Path(..., gt=0)):
#     # user = await crud.get(user_id)
#     # if not user:
#     #     raise HTTPException(status_code=404, detail="User not found")
#     # user_id = await crud.put(user_id, payload)
#     # return {**payload.dict(), "id": user_id}
#     pass
#
#
# @router.delete("/{user_id}", response_model=User)
# async def delete_user(user_id: int = Path(..., gt=0)):
#     # user = await crud.get(user_id)
#     # if not user:
#     #     raise HTTPException(status_code=404, detail="User not found")
#     # await crud.delete(user_id)
#     # return user
#     pass
