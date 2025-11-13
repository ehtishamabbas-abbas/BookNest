from fastapi import HTTPException, Depends
from app.core.security import verify_jwt_token
from app.database.connection import get_db 
from fastapi.security import OAuth2PasswordBearer 


# OAuth2 scheme to read Bearer token from Authorization header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login-user")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        email = await verify_jwt_token(token)
        db = get_db()
        collection = db["users"]
        existing_user = await collection.find_one({"email": email})
        if not existing_user:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")

        existing_user["id"] = str(existing_user.get("_id"))
        existing_user.pop("_id", None)
        existing_user.pop("password", None)

        return existing_user
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

async def require_admin(current_user = Depends(get_current_user)):
    role = (current_user.get("role") or "").lower()
    if role != "admin":
        raise HTTPException(status_code=403, detail="Admin can only access this endpoint")
    return current_user
