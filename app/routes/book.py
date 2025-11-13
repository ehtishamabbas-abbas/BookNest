from fastapi import APIRouter, Depends, HTTPException, status
from app.services.auth_services import get_current_user
from app.core.security import oauth2_scheme

router = APIRouter()

@router.post("/create-book", dependencies=[Depends(get_current_user(token=""))])
async def create_book(token: str = Depends(oauth2_scheme)):
    return {"message": "Book created successfully"}


