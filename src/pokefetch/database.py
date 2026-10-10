import os

from sqlalchemy import create_engine, text

DATABASE_URL = os.environ["DATABASE_URL"]
engine = create_engine(DATABASE_URL)


def test_database_connection() -> str:
    with engine.connect() as connection:
        return connection.execute(text("SELECT version()")).scalar_one()
