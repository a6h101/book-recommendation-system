from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.routes import router
from app.core.startup import load_resources

@asynccontextmanager
async def lifespan(app: FastAPI):
    # This runs when the server starts
    load_resources()
    yield
    # This runs when the server shuts down
    print("Shutting down...")

app = FastAPI(title="Book Recommendation System", lifespan=lifespan)
@app.get("/")
def root():
    return {"message": "Book Recommendation API is running"}

app.include_router(router)