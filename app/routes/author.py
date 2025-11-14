from fastapi import APIRouter, Depends
from app.dtos.book_dtos import AuthorDto
from app.middlewares.auth_middleware import require_admin
from app.controllers.authorController import handle_author_creation

router = APIRouter()


@router.post("/create-author")
async def create_author(author: AuthorDto, current_user = Depends(require_admin)): 
    user_id = current_user["id"]
    return await handle_author_creation(author, user_id)
