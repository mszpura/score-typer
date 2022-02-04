from typing import Type, List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.core.entities.abstract_entity import AbstractEntity, AbstractDto
from app.core.proxies import AbstractRepository


def create_crud_router_for(
        entity_type: Type[AbstractEntity],
        repository_factory: AbstractRepository,
        entity_dto_type: Type[AbstractDto]):
    router = APIRouter()

    @router.post("", response_model=entity_type, status_code=201)
    async def create(payload: entity_dto_type, repo: AbstractRepository = Depends(repository_factory)):
        entity = entity_type.create(**payload.dict())
        await repo.create(entity)
        return entity

    @router.get("/{id}", response_model=entity_type)
    async def get(
            id: UUID,
            repo: AbstractRepository = Depends(repository_factory)):
        entity = await repo.get(id)
        if not entity:
            raise HTTPException(status_code=404, detail=f"{entity_type.__name__} not found")
        return entity

    @router.get("", response_model=List[entity_type])
    async def get_all(repo: AbstractRepository = Depends(repository_factory)):
        return await repo.get_all()

    @router.put("", response_model=entity_type)
    async def update(id: UUID, payload: entity_dto_type, repo: AbstractRepository = Depends(repository_factory)):
        entity = await repo.get(id)
        if not entity:
            raise HTTPException(status_code=404, detail=f"{entity_type.__name__} not found")

        #todo
        return entity

    @router.delete("", response_model=entity_type)
    async def delete(id: UUID, repo: AbstractRepository = Depends(repository_factory)):
        entity = await repo.get(id)
        if not entity:
            raise HTTPException(status_code=404, detail=f"{entity_type.__name__} not found")
        await repo.delete(id)
        return entity

    @router.get("/qwe")
    async def qwe():
        return {"message": "test"}

    return router
