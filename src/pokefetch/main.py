from fastapi import FastAPI

from pokefetch.routes.pokemon import router as pokemon_router

app: FastAPI = FastAPI(title="PokeFetch API")


@app.get("/health", tags=["Health"])
async def health() -> dict[str, str]:
    return {"status": "PokeFetch healthy"}


app.include_router(pokemon_router)
