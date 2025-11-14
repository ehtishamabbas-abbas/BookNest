from fastapi import APIRouter, Depends 
from app.dtos.book_dtos import CreateBookDto, UpdateBookDto
from app.middlewares.auth_middleware import get_current_user, require_admin
from app.controllers.bookController import handle_book_creation, handle_get_all_books, handle_get_book, handle_delete_book, handle_update_book, handle_search_book_by_price
import logging

logger = logging.getLogger("uvicorn.error")
router = APIRouter()

@router.post("/create-book")
async def create_book(book: CreateBookDto, current_user = Depends(require_admin)): 
    user_id = current_user["id"]
    return await handle_book_creation(book, user_id)

@router.get("/get-all-books")
async def get_all_books(current_user = Depends(get_current_user)):
    return await handle_get_all_books(current_user["id"])

@router.get("/get-book/{book_id}")
async def get_book(book_id: str, current_user = Depends(get_current_user)):
    return await handle_get_book(book_id)

@router.delete("/delete-book/{book_id}")
async def delete_book(book_id: str, current_user = Depends(require_admin)):
    return await handle_delete_book(book_id)


@router.put("/update-book/{book_id}")
async def update_book(book_id: str, book: UpdateBookDto, current_user = Depends(require_admin)): 
    return await handle_update_book(book_id, book)

@router.get("/search-book-by-price")
async def search_book_by_price(min_price: float, max_price: float, current_user = Depends(get_current_user)):
    user_id = current_user["id"]
    return await handle_search_book_by_price(min_price, max_price, user_id)