from typing import Type, List, Callable, Awaitable
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.core.entities.abstract_entity import AbstractEntity, AbstractDto
from app.core.proxies import AbstractRepository


def create_crud_router_for(
        entity_type: Type[AbstractEntity],
        get_repository: Callable[[], AbstractRepository],
        input_data_type: Type[AbstractDto],
        custom_create_function: Callable[[AbstractDto], Awaitable[AbstractRepository]] = None,
        custom_update_function: Callable[[UUID, AbstractDto], Awaitable[AbstractRepository]] = None):
    router = APIRouter()

    @router.post("", response_model=entity_type, status_code=201)
    async def create(payload: input_data_type, repo: AbstractRepository = Depends(get_repository)):
        if custom_create_function:
            return await custom_create_function(payload)
        entity = entity_type.create(**payload.dict())
        await repo.create(entity)
        return entity

    @router.get("/{id}", response_model=entity_type)
    async def get(
            id: UUID,
            repo: AbstractRepository = Depends(get_repository)):
        entity = await repo.get(id)
        if not entity:
            raise HTTPException(status_code=404, detail=f"{entity_type.__name__} not found")
        return entity

    @router.get("", response_model=List[entity_type])
    async def get_all(repo: AbstractRepository = Depends(get_repository)):
        return await repo.get_all()

    @router.put("/{id}", response_model=entity_type)
    async def update(id: UUID, payload: input_data_type, repo: AbstractRepository = Depends(get_repository)):
        if custom_update_function:
            return await custom_update_function(id, payload)

        entity = await repo.get(id)
        if not entity:
            raise HTTPException(status_code=404, detail=f"{entity_type.__name__} not found")

        entity.update(**payload.dict())
        await repo.update(entity)
        return entity

    @router.delete("/{id}", response_model=entity_type)
    async def delete(id: UUID, repo: AbstractRepository = Depends(get_repository)):
        entity = await repo.get(id)
        if not entity:
            raise HTTPException(status_code=404, detail=f"{entity_type.__name__} not found")
        await repo.delete(id)
        return entity

    return router
