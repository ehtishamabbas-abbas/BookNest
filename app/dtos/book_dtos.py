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
    author: AuthorDto
    price: float
    edition: int
    category: str
    publisher: PublisherDto
    date_published: str


class UpdateBookDto(BaseModel): 
    title: Optional[str] = None
    author: Optional[AuthorDto] = None
    price: Optional[float] = None
    edition: Optional[int] = None
    category: Optional[str] = None
    publisher: Optional[PublisherDto] = None
    date_published: Optional[str] = None