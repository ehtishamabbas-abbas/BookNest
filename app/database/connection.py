from app.core.config import settings
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from typing import Optional
import logging

DATABASE_URL = settings.DATABASE_URL
DATABASE_NAME = settings.DATABASE_NAME

logger = logging.getLogger("uvicorn.error")

_client: Optional[AsyncIOMotorClient] = None
_db: Optional[AsyncIOMotorDatabase] = None


async def connect_to_db():
    global _client
    global _db
    try:
        if _client is not None:
            return

        _client = AsyncIOMotorClient(DATABASE_URL)
        _db = _client[DATABASE_NAME]

        # verify connection
        await _client.admin.command("ping")
        logger.info("Connected to database")
    except Exception as e:
        logger.exception("Failed to connect to database: %s", e)


def get_db() -> AsyncIOMotorDatabase:
    if _db is None:
        raise RuntimeError("Database not initialized. Ensure connect_to_db() runs on startup.")
    return _db


async def close_db():
    global _client
    global _db
    try:
        if _client is not None:
            _client.close()
            _client = None
            _db = None
            logger.info("Closed database connection")
    except Exception as e:
        logger.exception("Error while closing database connection: %s", e)
