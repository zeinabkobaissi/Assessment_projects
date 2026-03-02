from sqlalchemy import Boolean, Column, Integer, String
from database import Base
from pydantic import BaseModel

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    description = Column(String, index=True)
    genre= Column(String, index=True)
    publication_year = Column(Integer, index=True)
    
    #is_checked_out = Column(Boolean, default=False)  # 0 for not checked in, 1 for checked in
    
    


