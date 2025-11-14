from pydantic import BaseModel

class Author(BaseModel):
    name: str
    total_books: int
    age: int
    user_id: str
class Publisher(BaseModel):
    name: str
    country: str   
    total_books: int
    user_id: str

class CreateBookSchema(BaseModel):
    user_id: str
    title: str
    author_id: str
    price: float
    edition: int
    category: str
    publisher_id: str
    date_published: str


