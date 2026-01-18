from app.db.session import SessionLocal
from app.db.models import Book
import pandas as pd
import pickle
import os

# Globals (shared across app)
books_df = None
tfidf_matrix = None
tfidf_vectorizer = None


def load_resources():
    global books_df, tfidf_matrix, tfidf_vectorizer


    db = SessionLocal()
    books = db.query(Book).all()
    db.close()

    books_df = pd.DataFrame([{
        "id": b.id,
        "title": b.title,
        "author": b.author,
        "genres": b.genres,
        "description": b.description,
        "avg_rating": b.avg_rating
    } for b in books])

    # session artifacts loadup a6h1
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    ARTIFACTS_DIR = os.path.join(BASE_DIR, "ml", "artifacts")

    with open(os.path.join(ARTIFACTS_DIR, "tfidf_matrix.pkl"), "rb") as f:
        tfidf_matrix = pickle.load(f)

    with open(os.path.join(ARTIFACTS_DIR, "tfidf_vectorizer.pkl"), "rb") as f:
        tfidf_vectorizer = pickle.load(f)

    print("SQL + ML artifacts loaded")
