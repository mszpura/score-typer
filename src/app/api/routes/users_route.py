from typing import List
from uuid import UUID, uuid4

from fastapi import APIRouter, HTTPException, Depends
from app.adapters.repositories.users_repo import UsersRepository
from app.api.composition import compose_user_repository
from app.api.dtos.user_dto import UserDto
from app.core.entities.user import User

router = APIRouter()


@router.post("", response_model=User, status_code=201)
async def create_user(
        payload: UserDto,
        repo: UsersRepository = Depends(compose_user_repository)):
    user_id = uuid4()
    user = payload.to_domain(user_id)
    await repo.create(user)
    return user


@router.get("/{user_id}", response_model=User)
async def get_user(
        user_id: UUID,
        repo: UsersRepository = Depends(compose_user_repository)):
    user = await repo.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("", response_model=List[User])
async def get_all(repo: UsersRepository = Depends(compose_user_repository)):
    return await repo.get_all()


@router.put("/{user_id}", response_model=User)
async def update_user(
        user_id: UUID,
        payload: UserDto,
        repo: UsersRepository = Depends(compose_user_repository)):
    user = await repo.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.update(payload.username, payload.password, payload.email)
    await repo.update(user)
    return user


@router.delete("/{user_id}", response_model=User)
async def delete_user(
        user_id: UUID,
        repo: UsersRepository = Depends(compose_user_repository)):
    user = await repo.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await repo.delete(user_id)
    return user
