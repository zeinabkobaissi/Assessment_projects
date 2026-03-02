from sqlalchemy.orm import Session
from database import get_db
from model import Book
from schema import BookCreate

def create_book(db: Session, book: BookCreate):
    db_book = Book(
        title=book.title,
        author=book.author,
        description=book.description,
        genre=book.genre,
        publication_year=book.publication_year,
        
        
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_all_books(db: Session):
    return db.query(Book).all()

def update_book(db: Session, book_id: int, book: BookCreate):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        return None
    db_book.title = book.title
    db_book.author = book.author
    db_book.description = book.description
    db_book.genre = book.genre
    db_book.publication_year = book.publication_year
    
    
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        return None
    db.delete(db_book)
    db.commit()
    return db_book