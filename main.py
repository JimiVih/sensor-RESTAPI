from fastapi import FastAPI
from sqlmodel import SQLModel
from .routers import sensor_router, block_router
from .db.database import create_db_and_engine
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_engine()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(sensor_router.router)
app.include_router(block_router.router)
# @app.get("/test")
# async def testi():
#     return "moro"