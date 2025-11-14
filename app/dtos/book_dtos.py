from pydantic import BaseModel
from typing import Optional


class AuthorDto(BaseModel):
    name: Optional[str] = None
    total_books: Optional[int] = None
    age: Optional[int] = None

class PublisherDto(BaseModel):
    name: Optional[str] = None
    country: Optional[str] = None
    total_books: Optional[int] = None


class CreateBookDto(BaseModel): 
    title: str
    author_id: str
    price: float
    edition: int
    category: str
    publisher_id: str
    date_published: str


class UpdateBookDto(BaseModel): 
    title: Optional[str] = None
    author_id: Optional[str] = None
    price: Optional[float] = None
    edition: Optional[int] = None
    category: Optional[str] = None
    publisher_id: Optional[str] = None
    date_published: Optional[str] = None