from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:
    def __init__(self, df):
        self.df = df
        self.df["combined"] = (
            df["title"] + " " +
            df["authors"] + " " +
            df["genres"] + " " +
            df["description"]
        )

        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df["combined"])
        self.similarity = cosine_similarity(self.tfidf_matrix)

    def recommend_by_title(self, title, top_n=5):
        if title not in self.df["title"].values:
            return []

        idx = self.df[self.df["title"] == title].index[0]
        scores = list(enumerate(self.similarity[idx]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)

        return self.df.iloc[[i[0] for i in scores[1:top_n+1]]][
            ["title", "authors", "genres"]
        ].to_dict(orient="records")

    def recommend_by_genres(self, genres, top_n=5):
        query = " ".join(genres)
        query_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self.tfidf_matrix).flatten()

        top_indices = scores.argsort()[::-1][:top_n]
        return self.df.iloc[top_indices][
            ["title", "authors", "genres"]
        ].to_dict(orient="records")