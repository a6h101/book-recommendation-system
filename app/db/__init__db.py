import os
import pandas as pd

from app.db.session import engine, SessionLocal
from app.db.models import Book
from app.db.session import Base

# path fix
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
CSV_PATH = os.path.join(BASE_DIR, "ml", "cleaned_data", "books_cleaned.csv")


def init_db():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    print("Reading CSV...")
    df = pd.read_csv(CSV_PATH)

    print("Inserting data...")
    for _, row in df.iterrows():
        book = Book(
            title=row["Book"],
            author=row.get("Author"),
            description=row.get("Description"),
            genres=row.get("Genres"),
            avg_rating=row.get("Avg_Rating"),
            num_ratings=row.get("Num_Ratings"),
            thumbnail=row.get("URL"),
        )
        db.add(book)

    db.commit()
    db.close()

    print("Database initialized successfully!")


if __name__ == "__main__":
    init_db()
