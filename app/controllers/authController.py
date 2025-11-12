
from app.schemas.userSchema import CreateUserSchema


async def handle_register(user: CreateUserSchema):
    
    return {"message": "controller register"}