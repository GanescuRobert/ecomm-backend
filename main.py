import os
import uvicorn
from dotenv import load_dotenv
from app.main import app
from app.database.setup import create_models

create_models()

load_dotenv()

HOST = os.getenv("HOST", "0.0.0.0")
PORT = os.getenv("PORT", 8000)

if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=int(PORT))
