import os
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# loading artifacts
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
ARTIFACTS_DIR = os.path.join(BASE_DIR, "ml", "artifacts")

with open(os.path.join(ARTIFACTS_DIR, "books_df.pkl"), "rb") as f:
    book_df = pickle.load(f)

with open(os.path.join(ARTIFACTS_DIR, "tfidf_matrix.pkl"), "rb") as f:
    tfidf_matrix = pickle.load(f)

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

indices = pd.Series(book_df.index, index=book_df["Book"]).drop_duplicates()


def recommend_books(title: str, top_n: int = 5):
    """
    Returns list of book titles similar to input title
    """
    if title not in indices:
        return []

    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1: top_n + 1]

    return [book_df.iloc[i[0]]["Book"] for i in sim_scores]