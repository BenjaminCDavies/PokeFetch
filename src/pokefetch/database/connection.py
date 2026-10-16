from functools import lru_cache
from pathlib import Path
from typing import Any

from sqlalchemy import Engine, RowMapping, Sequence, TextClause, create_engine, text
from sqlalchemy.engine import URL

from pokefetch.constants import DATABASE_URL


@lru_cache(maxsize=64)
def load_query(query_name: str) -> str:
    """Load and cache a SQL query from the sql directory."""
    sql_dir: Path = Path(__file__).resolve().parent.parent / "sql"
    path: Path = Path(sql_dir / query_name).resolve()
    return path.read_text(encoding="utf-8")


class Database:
    def __init__(self, url: str | URL) -> None:
        self.engine: Engine = create_engine(url, pool_pre_ping=True)

    def fetch_one(
        self, query_name: str, params: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        query: TextClause = text(load_query(query_name))
        with self.engine.connect() as connection:
            row: RowMapping = connection.execute(query, params or {}).mappings().first()
        return dict(row) if row is not None else None

    def fetch_all(
        self, query_name: str, params: dict[str, Any] | None = None
    ) -> list[dict[str, Any]]:
        query: TextClause = text(load_query(query_name))
        with self.engine.connect() as connection:
            rows: Sequence[RowMapping] = (
                connection.execute(query, params or {}).mappings().all()
            )
        return [dict(row) for row in rows]

    def dispose(self) -> None:
        self.engine.dispose()


db = Database(DATABASE_URL)
