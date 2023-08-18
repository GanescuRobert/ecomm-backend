from fastapi import FastAPI
from app.api.routers import root, user

app = FastAPI()

app.include_router(root.router)
app.include_router(user.router)
