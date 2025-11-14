
from fastapi import APIRouter, Depends
from app.dtos.book_dtos import PublisherDto
from app.middlewares.auth_middleware import require_admin
from app.controllers.publisherController import handle_publisher_creation

router = APIRouter()

@router.post("/create-publisher")
async def create_publisher(publisher: PublisherDto, current_user = Depends(require_admin)): 
    user_id = current_user["id"]
    return await handle_publisher_creation(publisher, user_id)