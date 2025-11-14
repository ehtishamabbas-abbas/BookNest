from pydantic import HttpUrl
from app.schemas.bookSchema import CreateBookSchema 
from app.dtos.book_dtos import CreateBookDto, UpdateBookDto
import logging
from app.database.connection import get_db
from fastapi import HTTPException
from bson.objectid import ObjectId

logger = logging.getLogger("uvicorn.error")

async def create_book(book: CreateBookDto, user_id: str):
    try:
      
        db = get_db()
        collection = db["books"]
         
        book_schema = CreateBookSchema(user_id=user_id, **book.model_dump())
        book_object = book_schema.model_dump()
  
        result = await collection.insert_one(book_object) 

        book_object["id"] = str(result.inserted_id)
        book_object.pop("_id", None)

        return book_object
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create book: {str(e)}")


async def get_all_books(user_id: str):
    try:
        dg = get_db()
        collection = dg["books"]

        all_books = collection.find({"user_id": user_id})
        books = await all_books.to_list()

        for book in books:
            book["id"] = str(book.get("_id"))
            book.pop("_id", None)

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
    
async def update_book(book_id: str, book: UpdateBookDto):
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


async def search_book_by_price(min_price: float, max_price: float, user_id:str):
    try:
        db = get_db()
        collection = db["books"]

        pipeline = [
            {"$match": {"price": {"$gte": min_price, "$lte": max_price}}},
            # {"$project": {"category": 0}}, 
            {"$lookup": { "from": "authors","localField": "user_id","foreignField": "user_id","as": "authorData"}},
            {"$unwind": "$authorData"},
            {"$sort": {"title": -1}}
        ]
        result = await collection.aggregate(pipeline).to_list(length=None)  
 
        for book in result:
            book["id"] = str(book["_id"])
            book["authorData"]["id"] = str(book["authorData"]["_id"])
            book.pop("_id", None)
            book["authorData"].pop("_id", None)
 
        return {"data": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while finding the books based on min price: {str(e)}")

    