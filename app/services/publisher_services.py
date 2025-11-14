
from app.dtos.book_dtos import PublisherDto
from app.database.connection import get_db
from fastapi import HTTPException
from app.schemas.bookSchema import Publisher

async def create_publisher(publisher: PublisherDto, user_id: str):
    try:
        db = get_db()
        collection = db["publishers"]
        publisher = Publisher(user_id=user_id, **publisher.model_dump())
        publisher_result = await collection.insert_one(publisher.model_dump())
        publisher_id = str(publisher_result.inserted_id)
        return { "publisher_id": publisher_id }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create publisher: {str(e)}")