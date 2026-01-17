from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.routes import router
from app.core.startup import load_resources

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_resources()
    yield
    print("Shutting down...")

app = FastAPI(
    title="Book Recommendation API",
    lifespan=lifespan
    )

app.include_router(router)