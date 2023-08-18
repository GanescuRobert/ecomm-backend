from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database.session import Base
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_superuser = Column(Boolean, default=False)

    products = relationship("Product", back_populates="user")
    addresses = relationship("Address", back_populates="user")
    cart = relationship("Cart", back_populates="user")
    credit_cards = relationship("CreditCard", back_populates="user")
    orders = relationship("Order", back_populates="user")

    def verify_password(self, plain_password):
        return pwd_context.verify(plain_password, self.hashed_password)
