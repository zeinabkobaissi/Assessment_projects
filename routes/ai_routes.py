from services.ai_services import generate_book_summary, generate_book_recommendations
from fastapi import APIRouter, Depends, HTTPException, Request


router = APIRouter(prefix="/ai", tags=["AI"])

@router.get("/summary")
def book_summary_endpoint(request: Request, title: str, author: str):
    if request.session.get("role") != "admin" and request.session.get("role") != "user":
        raise HTTPException(status_code=403, detail="Not authorized")

    summary = generate_book_summary(title, author)
    return {"summary": summary}


@router.get("/recommendations")
def book_recommendations_endpoint(request: Request, title: str, author: str):
    if request.session.get("role") != "admin" and request.session.get("role") != "user":
        raise HTTPException(status_code=403, detail="Not authorized")

    recommendations = generate_book_recommendations(title, author)
    return {"recommendations": recommendations}