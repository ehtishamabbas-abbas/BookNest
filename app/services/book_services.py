from app.schemas.bookSchema import CreateBookSchema, UpdateBookSchema
import logging
from app.database.connection import get_db
from fastapi import HTTPException
from bson.objectid import ObjectId

logger = logging.getLogger("uvicorn.error")

async def create_book(book: CreateBookSchema):
    try:
        book = book.model_dump()
        db = get_db()
        collection = db["books"]
        result = await collection.insert_one(book)
        logger.info(f"Book created: {result.inserted_id}")
        book["id"] = str(result.inserted_id)
        book.pop("_id", None)

        return book
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create book: {str(e)}")


async def get_all_books():
    try:
        dg = get_db()
        collection = dg["books"]
        books = await collection.find().to_list(100)
        if books is None:
            raise HTTPException(status_code=404, detail="No books found")

        for book in books:
            book["id"] = str(book["_id"]) 
            book.pop("_id")

        return books
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get books: {str(e)}")
    
async def get_book(book_id: str):
    try:
        db = get_db()
        collection = db["books"]
        book = await collection.find_one({"_id": ObjectId(book_id)})
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        book["id"] = str(book["_id"])
        book.pop("_id")
        return book
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get book: {str(e)}")

async def delete_book(book_id: str):
    try:
        db = get_db()
        collection = db["books"]
        result = await collection.delete_one({"_id": ObjectId(book_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Book not found") 
        return {"message": "Book deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete book: {str(e)}")
    
async def update_book(book_id: str, book: UpdateBookSchema):
    try:
        db = get_db()
        collection = db["books"] 
        update_data = book.model_dump(exclude_unset=True)
        if not update_data:
            raise HTTPException(status_code=400, detail="No fields to update")
        result = await collection.update_one({"_id": ObjectId(book_id)}, {"$set": update_data})
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Book not found")
        return {"message": "Book updated successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update book: {str(e)}")


    