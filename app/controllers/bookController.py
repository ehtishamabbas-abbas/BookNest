from app.services.book_services import create_book
from app.schemas.bookSchema import CreateBookSchema 
from app.services.book_services import get_all_books, get_book, delete_book, update_book
from app.schemas.bookSchema import UpdateBookSchema

async def handle_book_creation(book: CreateBookSchema):
    return await create_book(book)

async def handle_get_all_books():
    return await get_all_books()

async def handle_get_book(book_id: str):
    return await get_book(book_id)

async def handle_delete_book(book_id: str):
    return await delete_book(book_id)

async def handle_update_book(book_id: str, book: UpdateBookSchema):
    return await update_book(book_id, book)
    



