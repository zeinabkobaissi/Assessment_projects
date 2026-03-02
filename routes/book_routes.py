from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from schema import BookCreate, BookResponse
from services.book_service import create_book, get_all_books, update_book, delete_book
from database import get_db
from services.ai_services import generate_book_summary, generate_book_recommendations


router= APIRouter(prefix='/books', tags=['Books'])

@router.post('/', response_model=BookResponse)

def create_book_endpoint(
    request: Request,
    book: BookCreate,
    db: Session = Depends(get_db)
):
    if request.session.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    return create_book(db, book)

@router.get('/', response_model=list[BookResponse])
def get_all_books_endpoint(request: Request, db: Session = Depends(get_db)):
    if request.session.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    return get_all_books(db)

@router.put('/{id}', response_model=BookResponse)
def update_book_endpoint(request: Request, id: int, book: BookCreate, db:Session = Depends(get_db)):
    if request.session.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    updated_book = update_book(db, id, book)
    if updated_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book


@router.delete('/{id}', response_model=BookResponse)
def delete_book_endpoint(request: Request, id: int, db:Session = Depends(get_db)):
    if request.session.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    deleted_book = delete_book(db, id)
    if deleted_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return deleted_book