from typing import Any

from fastapi import APIRouter, HTTPException

from pokefetch.repository.pokemon import pokemon_repository

router: APIRouter = APIRouter(prefix="/pokemon", tags=["Pokemon"])


@router.get("/{name}")
def get_pokemon(name: str) -> dict[str, Any]:
    pokemon: dict[str, Any] = pokemon_repository.get_by_name(name)
    if pokemon is None:
        raise HTTPException(
            status_code=404,
            detail=f"Pokemon '{name}' not found",
        )
    return pokemon


@router.get("")
def list_pokemon(
    limit: int = 50,
    offset: int = 0,
) -> list[dict[str, Any]]:
    if not 1 <= limit <= 100:
        raise HTTPException(
            status_code=422,
            detail="Limit must be between 1 and 100",
        )
    if offset < 0:
        raise HTTPException(
            status_code=422,
            detail="Offset cannot be negative",
        )

    return pokemon_repository.list_all(limit, offset)
