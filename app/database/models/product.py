from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship
from app.database.session import Base


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    SKU = Column(String, index=True)
    price = Column(Float)
    delivery_time = Column(String)
    is_active = Column(Boolean, default=True)

    user = relationship("User", back_populates="products")
    images = relationship("ProductImage", back_populates="product")
    cart_items = relationship("CartItem", back_populates="product")
    product_attributes = relationship("ProductAttributes", back_populates="product")
