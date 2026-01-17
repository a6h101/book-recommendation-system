from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # dev only
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)