from typing import List
from uuid import UUID, uuid4

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.db.config import get_session
from app.adapters.repositories import users_repo
from app.api.dtos.user_dto import UserDto
from app.core.entities.user import User

router = APIRouter()


@router.post("", response_model=User, status_code=201)
async def create_user(
        payload: UserDto,
        session: AsyncSession = Depends(get_session)):
    user_id = uuid4()
    user = payload.to_domain(user_id)
    await users_repo.create(user, session)
    return user


@router.get("/{user_id}", response_model=User)
async def get_user(
        user_id: UUID,
        session: AsyncSession = Depends(get_session)):
    user = await users_repo.get(user_id, session)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("", response_model=List[User])
async def get_all(session: AsyncSession = Depends(get_session)):
    return await users_repo.get_all(session)


@router.put("/{user_id}", response_model=User)
async def update_user(user_id: UUID, payload: UserDto, session: AsyncSession = Depends(get_session)):
    user = await users_repo.get(user_id, session)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.update(payload.username, payload.password, payload.email)
    await users_repo.update(user, session)
    await session.commit()
    return user


@router.delete("/{user_id}", response_model=User)
async def delete_user(user_id: UUID, session: AsyncSession = Depends(get_session)):
    user = await users_repo.get(user_id, session)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await users_repo.delete(user_id, session)
    await session.commit()
    return user
