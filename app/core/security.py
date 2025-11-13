
from passlib.context import CryptContext 
import logging
from datetime import datetime, timedelta, timezone
import jwt
from app.core.config import settings
from fastapi import HTTPException 

logger = logging.getLogger("uvicorn.error")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

TOKEN_EXPIRE = settings.TOKEN_EXPIRE
JWT_ALGORITHM = settings.JWT_ALGORITHM
SECRET_KEY = settings.SECRET_KEY


async def get_password_hash(password: str):
    return pwd_context.hash(password)

async def verify_password(plain_password, hashed_password): 
    return pwd_context.verify(plain_password, hashed_password)  

async def create_jwt_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=TOKEN_EXPIRE)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt

async def verify_jwt_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload["email"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired, please login again")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token, please login again")