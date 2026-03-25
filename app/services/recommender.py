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
    title_norm = normalize(title)

    exact_match = book_df[book_df["book_norm"] == title_norm]

    if exact_match.empty:
        matches = book_df[book_df["book_norm"].str.contains(title_norm, na=False)]
        if matches.empty:
            return []
        idx = matches.index[0]
    else:
        idx = exact_match.index[0]

    sim_scores = cosine_sim[idx]
    top_idx = sim_scores.argsort()[-top_n-1:-1][::-1]

    return book_df.loc[top_idx, "Book"].tolist()