from app.db.session import SessionLocal
from app.db.models import Book
import pandas as pd
from app.services.recommender import Recommender

recommender = None

def load_resources():
    global recommender

    db = SessionLocal()
    books = db.query(Book).all()
    db.close()

    data = [{
        "id": b.serial_no,
        "title": b.book,
        "authors": b.author,
        "genres": b.genres,
        "description": b.description
    } for b in books]

    df = pd.DataFrame(data)
    recommender = Recommender(df)