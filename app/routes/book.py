from fastapi import APIRouter, Depends 
from app.schemas.bookSchema import CreateBookSchema, UpdateBookSchema
from app.middlewares.auth_middleware import get_current_user
from app.controllers.bookController import handle_book_creation, handle_get_all_books, handle_get_book, handle_delete_book, handle_update_book
import logging

logger = logging.getLogger("uvicorn.error")
router = APIRouter()

@router.post("/create-book")
async def create_book(book: CreateBookSchema, current_user = Depends(get_current_user)): 
    return await handle_book_creation(book)

@router.get("/get-all-books")
async def get_all_books(current_user = Depends(get_current_user)):
    return await handle_get_all_books()

@router.get("/get-book/{book_id}")
async def get_book(book_id: str, current_user = Depends(get_current_user)):
    return await handle_get_book(book_id)

@router.delete("/delete-book/{book_id}")
async def delete_book(book_id: str, current_user = Depends(get_current_user)):
    return await handle_delete_book(book_id)


@router.put("/update-book/{book_id}")
async def update_book(book_id: str, book: UpdateBookSchema, current_user = Depends(get_current_user)):
    return await handle_update_book(book_id, book)
