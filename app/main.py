from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Book Recommendation System")

app.include_router(router)
