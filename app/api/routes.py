from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from urllib.parse import quote_plus

from app.services.recommender import recommend_books
from app.db.session import get_db
from app.db.models import Book

router = APIRouter()


def make_thumbnail(book: Book) -> str:
    title = quote_plus(book.title)
    return f"https://covers.openlibrary.org/b/title/{title}-L.jpg"


@router.get("/recommend")
def recommend(title: str, db: Session = Depends(get_db)):
    titles = recommend_books(title)

    if not titles:
        return []

    books = (
        db.query(Book)
        .filter(Book.title.in_(titles))
        .limit(10)
        .all()
    )

    return [
        {
            "title": b.title,
            "author": b.author,
            "avg_rating": b.avg_rating,
            "url": b.thumbnail,
            "thumbnail": make_thumbnail(b),
        }
        for b in books
    ]