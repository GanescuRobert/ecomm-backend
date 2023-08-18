from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database.session import Base


class ProductAttributes(Base):
    __tablename__ = "product_attributes"

    product_attributes_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.product_id"))
    color_id = Column(Integer, ForeignKey("colors.color_id"))
    size_id = Column(Integer, ForeignKey("sizes.size_id"))

    product = relationship("Product", back_populates="product_attributes")

    color = relationship("Color")
    size = relationship("Size")
