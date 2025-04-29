from fastapi import APIRouter
from app.services.db_service import fetch_all_tables

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.get("/data")
def get_data():
    return fetch_all_tables()