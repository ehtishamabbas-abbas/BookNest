from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

def create_app() -> FastAPI:
    app = FastAPI(title=settings.APP_NAME)

     # cors 
    app.add_middleware(
        CORSMiddleware, 
        allow_regoins=["*"]
    )

    # register the routes


   
    @app.get("/")
    async def root():
        return {"message": "backend is up"}

    return app

