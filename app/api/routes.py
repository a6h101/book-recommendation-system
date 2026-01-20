from fastapi import APIRouter, Query
from app.core.startup import recommender

router = APIRouter(prefix="recommend", tags=["recommendations"])

@router.get("/title")
def recommend_by_title(book : str):
    results = recommender.recommend_by_title(book)
    if not results:
        return {"message": "Book not found!"}
    return {"recommendations": results}

@router.get("/genres")
def recommend_by_genres(genres: list[str] = Query(...)):
    results = recommender.recommend_by_genres(genres)
    return {"recommnedation": results}