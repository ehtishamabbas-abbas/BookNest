from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings 
from app.routes.auth import router as auth_router
from app.routes.book import router as book_router
from app.routes.author import router as author_router
from app.routes.publisher import router as publisher_router
from app.database.connection import connect_to_db, close_db  

app = FastAPI(title=settings.APP_NAME)

 # cors 
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"]
)

@app.on_event("startup")
async def on_startup():
    await connect_to_db()  

@app.on_event("shutdown")
async def on_shutdown():
    await close_db()

# register the public routes 
app.include_router(auth_router, prefix="/api")

# register the protected routes 
app.include_router(book_router, prefix="/api")
app.include_router(author_router, prefix="/api")
app.include_router(publisher_router, prefix="/api")


@app.get("/")
async def root():
    return {"message": "backend is up"}


def create_app() -> FastAPI:
    return app

