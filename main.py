from schema import BookCreate
from routes.book_routes import router as book_router
from fastapi import FastAPI, Request, Depends
from database import engine, Base, get_db
from routes.auth_routes import router as auth_router
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from services.book_service import get_all_books
from routes.ai_routes import router as ai_router

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Library Management System")


app.add_middleware(SessionMiddleware, secret_key="your_secret_key_here")



app.include_router(book_router)
app.include_router(auth_router)
app.include_router(ai_router)

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):

    if "user" not in request.session:
        return RedirectResponse("/login", status_code=303)

    books = get_all_books(db)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "books": books,
            "role": request.session.get("role")
        }
    )
    
@app.get("/home", response_class=HTMLResponse)
def home_page(request: Request, db: Session = Depends(get_db)):
    if "user" not in request.session:
        return RedirectResponse("/login", status_code=303)

    books = get_all_books(db)

    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "books": books,
            "role": request.session.get("role")
        }
    )