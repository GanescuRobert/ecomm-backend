from sqlalchemy import Column, Integer, String
from app.database.session import Base


class Size(Base):
    __tablename__ = "sizes"

    size_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
