"""Transactions Service main entry point."""

from fastapi import FastAPI
from app.core.config import settings
from app.core.db import init_db
from app.api.bills import router as bills_router
from app.api.vendors import router as vendors_router

def lifespan(_ : FastAPI):
    """Lifespan event for the FastAPI app."""
    # Initialize the database
    init_db()
    yield


app = FastAPI(
    title=settings.API_NAME,
    description="Transactions Service for accounting application",
    lifespan=lifespan,
)

app.include_router(bills_router)
app.include_router(vendors_router)

@app.get("/", tags=["root"])
async def root():
    """Root endpoint."""
    return {"message": "Welcome to the Transactions Service!"}
