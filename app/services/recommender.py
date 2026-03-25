import os
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
ARTIFACTS_DIR = os.path.join(BASE_DIR, "ml", "artifacts")

with open(os.path.join(ARTIFACTS_DIR, "books_df.pkl"), "rb") as f:
    book_df = pickle.load(f)

    print("BOOK_DF COLUMNS:", book_df.columns.tolist()) #debug line for columns

with open(os.path.join(ARTIFACTS_DIR, "tfidf_matrix.pkl"), "rb") as f:
    tfidf_matrix = pickle.load(f)

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def normalize(text: str):
    return text.lower().strip()

book_df["book_norm"] = book_df["Book"].str.lower().str.strip()

def recommend_books(title: str, top_n: int = 5):
    title = title.lower().strip()

    matches = book_df[book_df["Book"].str.lower().str.contains(title, na=False)]

    if matches.empty:
        return []

    idx = matches.index[0]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    recommendations = []

    for i, score in sim_scores[1: top_n+1]:
        book = book_df.iloc[i]

        recommendations.append({
            "title": book.get("Book", ""),
            "author": book.get("Author", ""),
            "avg_rating": book.get("Avg_Rating", 0),
            "thumbnail": book.get("URL", "")
        })

    return recommendations


