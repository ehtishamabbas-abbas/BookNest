
from app.services.publisher_services import create_publisher
from app.dtos.book_dtos import PublisherDto

async def handle_publisher_creation(publisher: PublisherDto, user_id: str):
    return await create_publisher(publisher, user_id)