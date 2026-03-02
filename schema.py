from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    description: str
    genre: str
    publication_year: int
    
    
    

class BookResponse(BookCreate):
    id: int

    