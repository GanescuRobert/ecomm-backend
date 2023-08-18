from app.database.session import Base, engine
from app.database.models.user import User
from app.database.models.product import Product
from app.database.models.address import Address
from app.database.models.cart import Cart
from app.database.models.credit_card import CreditCard
from app.database.models.order import Order
from app.database.models.product_image import ProductImage
from app.database.models.product_attributes import ProductAttributes
from app.database.models.cart_item import CartItem
from app.database.models.order_item import OrderItem
from app.database.models.color import Color
from app.database.models.size import Size


def create_models():

    Base.metadata.create_all(bind=engine)
