from fastapi import APIRouter
from app.controllers.authController import handle_register, handle_login
from app.schemas.userSchema import CreateUserSchema, LoginUserSchema

router = APIRouter()

@router.post("/register-user")
async def register(
    user: CreateUserSchema
):
        return await handle_register(user)

@router.post("/login-user")
async def login(
    user: LoginUserSchema
):
    return await handle_login(user)