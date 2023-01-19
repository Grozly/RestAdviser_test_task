from fastapi import APIRouter

from app.api.endpoints import signal


api_router = APIRouter()
api_router.include_router(signal.router, prefix="/signal")
