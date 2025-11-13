from app.services.auth_services import register_user, login_user
from app.schemas.userSchema import CreateUserSchema, LoginUserSchema


async def handle_register(user: CreateUserSchema):
    return await register_user(user)

async def handle_login(user: LoginUserSchema):
    return await login_user(user)