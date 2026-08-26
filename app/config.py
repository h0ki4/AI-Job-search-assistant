import os
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DATABASE_PATH = PROJECT_ROOT / "data" / "job_search.db"


def get_database_path() -> Path:
    """Return an absolute SQLite path derived from the process environment."""
    configured_path = os.environ.get("DATABASE_PATH")
    if configured_path is None:
        return DEFAULT_DATABASE_PATH

    database_path = Path(configured_path).expanduser()
    if database_path.is_absolute():
        return database_path

    return PROJECT_ROOT / database_path
