from fastapi import HTTPException
from app.schemas.userSchema import CreateUserSchema, LoginUserSchema
from app.database.connection import get_db
import logging
from app.core.security import get_password_hash, verify_password, create_jwt_access_token 

logger = logging.getLogger("uvicorn.error")

async def register_user(user: CreateUserSchema):
    try:
        db = get_db()   
        collection = db["users"]

        existing_user = await collection.find_one({"email": user.email})
        if existing_user:
            raise HTTPException(status_code=400, detail="User already exists")
        else:
            token = await create_jwt_access_token({"email": user.email})
            user.password = await get_password_hash(user.password)
            user = user.model_dump()
            await collection.insert_one(user) 

            return {"token": token}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def login_user(user: LoginUserSchema):
    try: 
        db = get_db()
        collection = db["users"]
        existing_user = await collection.find_one({"email": user.email})
        
        if not existing_user:
            raise HTTPException(status_code=400, detail="User not found")

        is_password_valid = await verify_password(user.password, existing_user["password"]) 
        if is_password_valid is not True:
            raise HTTPException(status_code=400, detail="Incorrect password")

        # add id to existing_user
        existing_user["id"] = str(existing_user["_id"])
        existing_user.pop("_id") 

        token = await create_jwt_access_token({"email": user.email}) 
    
        return {"token": token}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
