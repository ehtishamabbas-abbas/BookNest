from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME")
    APP_ENV = os.getenv("APP_ENV")
    DATABASE_URL = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
    DATABASE_NAME = os.getenv("DATABASE_NAME")
    TOKEN_EXPIRE = int(os.getenv("TOKEN_EXPIRE", "15"))

settings = Settings()


