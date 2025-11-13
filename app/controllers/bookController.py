from app.services.book_services import create_book
from app.dtos.book_dtos import CreateBookDto, UpdateBookDto
from app.services.book_services import get_all_books, get_book, delete_book, update_book 

async def handle_book_creation(book: CreateBookDto, user_id: str):
    return await create_book(book, user_id)

async def handle_get_all_books(user_id: str):
    return await get_all_books(user_id)

async def handle_get_book(book_id: str):
    return await get_book(book_id)

async def handle_delete_book(book_id: str):
    return await delete_book(book_id)

async def handle_update_book(book_id: str, book: UpdateBookDto):
    return await update_book(book_id, book)
    



