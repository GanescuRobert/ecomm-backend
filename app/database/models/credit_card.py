from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.session import Base


class CreditCard(Base):
    __tablename__ = "credit_cards"

    credit_card_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    card_number = Column(String)
    expiration_date = Column(String)
    cardholder_name = Column(String)
    cvv = Column(String)

    customer = relationship("Customer", back_populates="credit_cards")
