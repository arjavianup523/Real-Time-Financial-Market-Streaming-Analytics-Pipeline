from pathlib import Path
import os

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"


load_dotenv(PROJECT_ROOT / ".env")


TWELVE_DATA_API_KEY = os.getenv("TWELVE_DATA_API_KEY")

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


if not TWELVE_DATA_API_KEY:
    raise ValueError(
        "TWELVE_DATA_API_KEY is missing. "
        "Add it to the .env file."
    )


if not DB_HOST:
    raise ValueError(
        "DB_HOST is missing. "
        "Add the MySQL settings to the .env file."
    )


if not DB_USER:
    raise ValueError(
        "DB_USER is missing. "
        "Add the MySQL settings to the .env file."
    )


if not DB_NAME:
    raise ValueError(
        "DB_NAME is missing. "
        "Add the MySQL settings to the .env file."
    )