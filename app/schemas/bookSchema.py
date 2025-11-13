from pydantic import BaseModel

class Author(BaseModel):
    name: str
    total_books: int
    age: int
class Publisher(BaseModel):
    name: str
    country: str   
    total_books: int

class CreateBookSchema(BaseModel):
    user_id: str
    title: str
    author: Author
    price: float
    edition: int
    category: str
    publisher: Publisher
    date_published: str


