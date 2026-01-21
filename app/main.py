from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.routes import router as api_router
from app.core.startup import load_resources
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_resources()
    yield
    print("Shutting down...")

app = FastAPI(title="Book Recommendation System", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Book Recommendation API is running"}

app.include_router(api_router)