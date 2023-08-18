import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self):
        self.JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
        self.JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
        self.JWT_EXPIRATION_HOURS = int(os.getenv("JWT_EXPIRATION_HOURS"))


settings = Settings()
