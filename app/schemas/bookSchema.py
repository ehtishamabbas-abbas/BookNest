from typing import Optional
from pydantic import BaseModel


class Author(BaseModel):
    name: Optional[str] = None
    total_books: Optional[int] = None
    age: Optional[int] = None 


class Publisher(BaseModel):
    name: Optional[str] = None
    country: Optional[str] = None
    total_books: Optional[int] = None
    


class CreateBookSchema(BaseModel):
    title: str
    author: Author
    price: float
    edition: int
    category: str
    publisher: Publisher
    date_published: str


class UpdateBookSchema(BaseModel):
    title: Optional[str] = None
    author: Optional[Author] = None
    price: Optional[float] = None
    edition: Optional[int] = None
    category: Optional[str] = None
    publisher: Optional[Publisher] = None
    date_published: Optional[str] = None

