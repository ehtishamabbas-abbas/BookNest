from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings 
from app.routes.auth import router as auth_router

def create_app() -> FastAPI:
    app = FastAPI(title=settings.APP_NAME)

     # cors 
    app.add_middleware(
        CORSMiddleware, 
        allow_origins=["*"]
    )

    # register the routes
    app.include_router(auth_router, prefix="/api")


   
    @app.get("/")
    async def root():
        return {"message": "backend is up"}

    return app

