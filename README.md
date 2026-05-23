# Book Recommendation System(In progress)

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?style=for-the-badge&logo=scikit-learn)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)

A content-based book recommendation engine that suggests similar books based on metadata using TF-IDF vectorization and cosine similarity.

> 🔗 GitHub: [github.com/a6h101](https://github.com/a6h101)

---

## What It Does

- User inputs a book title
- System finds the most similar books based on content features
- Returns top N recommendations ranked by similarity score

---

## How It Works

**TF-IDF Vectorization**
Converts book metadata (title, author, genre, description) into numerical vectors. Words that appear frequently in one book but rarely across all books get higher weight — capturing what makes each book unique.

**Cosine Similarity**
Measures the angle between two book vectors. Books pointing in the same direction in vector space are considered similar. A score of 1.0 means identical, 0.0 means completely different.

```
User inputs book → TF-IDF vector → cosine similarity against all books → top matches returned
```

---


## Run Locally

```bash
# Clone the repo
git clone https://github.com/a6h101/book-recommendation.git
cd book-recommendation

# Create environment
conda create -n book-recommender python=3.10
conda activate book-recommender

# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn main:app --reload
```

API will be live at `http://localhost:8000`

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas | Data loading and preprocessing |
| Scikit-learn | TF-IDF vectorization, cosine similarity |
| FastAPI | REST API for serving recommendations |
| SQL | Data storage and querying |

---

## 📄 Dataset

Real-world book dataset with 10K+ records including titles, authors, and metadata.
