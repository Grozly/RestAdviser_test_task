import logging
from logging.config import dictConfig

from fastapi import FastAPI

from app import schemas
from app.api.api import api_router


dictConfig(schemas.LogConfig().dict())
logger = logging.getLogger("RestAdviser")


app = FastAPI(title="Signal")
app.include_router(api_router, tags=["signal"])

logger.info("Server started!")
