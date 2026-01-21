from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services.recommender import recommend_books
from app.db.session import get_db
from app.db.models import Book
#router
router = APIRouter()

@router.get("/recommend")
def recommend(title: str, db: Session = Depends(get_db)):
    titles = recommend_books(title)

    if not titles:
        return {"message": "No recommendations found"}

    books = db.query(Book).filter(Book.title.in_(titles)).all()

    return books