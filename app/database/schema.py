"""SQLite schema initialization for the application database."""

import aiosqlite


SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS vacancies (
    id INTEGER PRIMARY KEY,
    position TEXT NOT NULL,
    company TEXT NOT NULL,
    country_code TEXT,
    city TEXT,
    work_format TEXT NOT NULL DEFAULT 'unknown'
        CHECK (work_format IN ('remote', 'hybrid', 'office', 'unknown')),
    status TEXT NOT NULL DEFAULT 'saved'
        CHECK (status IN (
            'saved',
            'applied',
            'interview',
            'offer',
            'rejected',
            'archived'
        )),
    notes TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS vacancy_listings (
    id INTEGER PRIMARY KEY,
    vacancy_id INTEGER NOT NULL,
    platform TEXT NOT NULL,
    url TEXT NOT NULL,
    external_id TEXT,
    position_raw TEXT,
    company_raw TEXT,
    location_raw TEXT,
    description TEXT,
    publication_date TEXT,
    first_seen_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_seen_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (vacancy_id) REFERENCES vacancies(id) ON DELETE CASCADE,
    UNIQUE(platform, url),
    UNIQUE(platform, external_id)
);
"""


async def initialize_database(connection: aiosqlite.Connection) -> None:
    """Create the initial schema if it has not already been created."""
    await connection.execute("PRAGMA foreign_keys = ON")
    await connection.executescript(SCHEMA_SQL)
    await connection.commit()
