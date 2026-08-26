from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from pathlib import Path

import aiosqlite


@asynccontextmanager
async def open_database(
    database_path: Path,
) -> AsyncIterator[aiosqlite.Connection]:
    """Open one SQLite connection and close it after the caller finishes."""
    async with aiosqlite.connect(database_path) as connection:
        await connection.execute("PRAGMA foreign_keys = ON")
        yield connection
