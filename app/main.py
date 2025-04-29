from fastapi import FastAPI
from app.api.endpoints import router as v1_router
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)


app.include_router(v1_router, prefix="/api")