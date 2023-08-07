from fastapi import FastAPI
from app.api.routers import root


app = FastAPI()

app.include_router(root.router)
