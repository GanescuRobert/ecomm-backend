from sqlalchemy import Column, Integer, String
from app.database.session import Base


class Color(Base):
    __tablename__ = "colors"

    color_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
