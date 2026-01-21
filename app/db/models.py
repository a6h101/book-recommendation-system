from sqlalchemy import Column, Integer, String, Float, Text
from app.db.session import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255), index=True, nullable=False)
    author = Column(String(255), nullable=True)

    description = Column(Text, nullable=True)
    genres = Column(Text, nullable=True)

    avg_rating = Column(Float, nullable=True)
    num_ratings = Column(Integer, nullable=True)

    thumbnail = Column(String(500), nullable=True)