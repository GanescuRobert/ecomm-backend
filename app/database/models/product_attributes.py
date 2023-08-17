from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database.session import Base

class ProductAttribute(Base):
    __tablename__ = "product_attributes"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    color_id = Column(Integer, ForeignKey("colors.id"))
    size_id = Column(Integer, ForeignKey("sizes.id"))
    
    product = relationship("Product", back_populates="attributes")
    color = relationship("Color")
    size = relationship("Size")