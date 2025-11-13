

from datetime import datetime


class Author(BaseModel):
    name: str
    total_books: int
    age: int 


class Publisher(BaseModel):
    name: str
    country: str
    total_books: int
    


class CreateBookSchema(BaseModel):
    title: str
    author: Author
    price: float
    edition: int
    category: str
    publisher: Publisher
    date_published: datetime
    

