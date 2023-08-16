from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database.session import Base


class Merchandiser(Base):
    __tablename__ = "merchandisers"

    merchandiser_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))

    user = relationship("User", back_populates="merchandisers")
    products = relationship("Product", back_populates="merchandiser")
