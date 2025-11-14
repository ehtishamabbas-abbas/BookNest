from app.dtos.book_dtos import AuthorDto
from app.database.connection import get_db
from fastapi import HTTPException
from app.schemas.bookSchema import Author

async def create_author(author: AuthorDto, user_id: str):
    try:
        db = get_db()
        collection = db["authors"]
        author = Author(user_id=user_id, **author.model_dump())
        author_result = await collection.insert_one(author.model_dump())
        author_id = str(author_result.inserted_id)
        return {"author_id": author_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create author: {str(e)}")