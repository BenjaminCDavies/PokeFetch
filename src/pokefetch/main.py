from fastapi import FastAPI

from pokefetch.database import test_database_connection

app = FastAPI()


@app.get("/health", tags=["Health"])
async def health():
    return {"status": "PokeFetch healthy"}


@app.get("/db")
def db():
    return {"database": test_database_connection()}
