from app.services.author_services import create_author
from app.dtos.book_dtos import AuthorDto

async def handle_author_creation(author: AuthorDto, user_id: str):
    return await create_author(author, user_id)