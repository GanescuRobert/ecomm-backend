from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.session import Base


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    email = Column(String)

    user = relationship("User", back_populates="customers")
    addresses = relationship("Address", back_populates="customer")
    credit_cards = relationship("CreditCard", back_populates="customer")
    carts = relationship("Cart", back_populates="customer")
