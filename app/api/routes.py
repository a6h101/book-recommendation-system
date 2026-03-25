from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from urllib.parse import quote_plus
import requests
from app.services.recommender import recommend_books
from app.db.session import get_db
from app.db.models import Book
import re

def clean_title(title):
    return re.sub(r"\(.*?\)", "", title).strip()

router = APIRouter()


def make_thumbnail(title: str):
    cleaned = clean_title(title)
    query = quote_plus(cleaned)

    url = f"https://www.googleapis.com/books/v1/volumes?q=intitle:{query}"

    try:
        res = requests.get(url)
        data = res.json()

        if "items" in data:
            volume = data["items"][0]
            image_links = volume["volumeInfo"].get("imageLinks", {})

            thumbnail = image_links.get("thumbnail")

            if thumbnail:
                return thumbnail.replace("http://", "https://")

    except Exception as e:
        print("Google Books error:", e)

    return "images/default-book.jpg"


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
            "thumbnail": make_thumbnail(b.title),
        }
        for b in books
    ]