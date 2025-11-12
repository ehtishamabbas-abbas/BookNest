from fastapi import APIRouter
from app.controllers.authController import handle_register
from app.schemas.userSchema import CreateUserSchema

router = APIRouter()

@router.post("/register")
async def register(
    user: CreateUserSchema
):
    return await handle_register(user)