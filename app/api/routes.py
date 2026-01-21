from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services.recommender import recommend_books
from app.db.session import get_db
from app.db.models import Book

router = APIRouter()

@router.get("/recommend")
def recommend(title: str):
    recommendations = recommend_books(title)

    if not recommendations:
        return []

    return recommendations
