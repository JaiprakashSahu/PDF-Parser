from fastapi import FastAPI
from app.api.endpoints import health
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(health.router, prefix="/api", tags=["health"])

@app.get("/")
def root():
    return {"message": f"Welcome to {settings.PROJECT_NAME}"}
