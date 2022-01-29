from typing import List
from fastapi import APIRouter, HTTPException, Path

from app.api import crud
from app.api.dtos.user_dto import UserDto, UserDb

router = APIRouter()


@router.post("", response_model=UserDb, status_code=201)
async def create_user(payload: UserDto):
    user_id = await crud.post(payload)

    return {**payload.dict(), "id": user_id}


@router.get("/{user_id}", response_model=UserDb)
async def get_user(user_id: int = Path(..., gt=0)):
    user = await crud.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("", response_model=List[UserDb])
async def get_all():
    return await crud.get_all()


@router.put("/{user_id}", response_model=UserDb)
async def update_user(payload: UserDto, user_id: int = Path(..., gt=0)):
    user = await crud.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user_id = await crud.put(user_id, payload)
    return {**payload.dict(), "id": user_id}


@router.delete("/{user_id}", response_model=UserDb)
async def delete_user(user_id: int = Path(..., gt=0)):
    user = await crud.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await crud.delete(user_id)
    return user
