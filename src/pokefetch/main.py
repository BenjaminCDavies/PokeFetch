from fastapi import FastAPI, HTTPException
from sqlalchemy import Engine, TextClause, create_engine, text

from pokefetch.constants import DATABASE_URL

app: FastAPI = FastAPI(title="PokeFetch API")

engine: Engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)


@app.get("/health", tags=["Health"])
async def health() -> dict[str, str]:
    return {"status": "PokeFetch healthy"}


@app.get("/pokemon/{name}")
def get_pokemon(name: str):
    query: TextClause = text(
        "SELECT * FROM pokemon WHERE LOWER(name) = LOWER(:name) LIMIT 1"
    )

    with engine.connect() as connection:
        pokemon = connection.execute(query, {"name": name}).mappings().first()
    if pokemon is None:
        raise HTTPException(
            status_code=404,
            detail=f"Pokemon '{name}' not found",
        )
    return dict(pokemon)
