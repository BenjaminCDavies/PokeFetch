import os

from sqlalchemy import create_engine, text
from sqlalchemy.exc import ArgumentError


def test_database_connection() -> str:
    try:
        DATABASE_URL = os.environ["DATABASE_URL"]
        engine = create_engine(DATABASE_URL)
        with engine.connect() as connection:
            return connection.execute(text("SELECT version()")).scalar_one()
    except ArgumentError as e:
        return e
