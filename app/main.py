import asyncio

from app.config import get_database_path
from app.database.connection import open_database
from app.database.schema import initialize_database


async def main() -> None:
    """Start the application and verify its asynchronous SQLite connection."""
    event_loop = asyncio.get_running_loop()
    database_path = get_database_path()

    async with open_database(database_path) as connection:
        await initialize_database(connection)
        async with connection.execute("SELECT sqlite_version()") as cursor:
            row = await cursor.fetchone()

    sqlite_version = row[0] if row is not None else "unknown"
    print("AI Job Search Assistant started")
    print(f"Event loop: {type(event_loop).__name__}")
    print(f"SQLite connection: OK (version {sqlite_version})")
    print("Schema: vacancies, vacancy_listings")
    print(f"Database: {database_path}")


if __name__ == "__main__":
    asyncio.run(main())
