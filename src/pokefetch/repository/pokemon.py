from typing import Any

from pokefetch.database.connection import db


class PokemonRepository:
    def get_by_name(self, name: str) -> dict[str, Any] | None:
        return db.fetch_one(
            "get_by_name.sql",
            {"name": name},
        )

    def list_all(
        self,
        limit: int = 50,
        offset: int = 0,
    ) -> list[dict[str, Any]]:
        return db.fetch_all(
            "list_all.sql",
            {"limit": limit, "offset": offset},
        )


pokemon_repository: PokemonRepository = PokemonRepository()
