from fastapi import FastAPI
from app.api.routers import root
from app.database import setup

setup.create_models()

app = FastAPI()

app.include_router(root.router)
