from app.database.session import engine
from app.database.models import (
    user,
    customer,
    merchandiser,
    product,
    product_image,
    cart,
    cart_item,
    address,
    credit_card,
)


def create_models():
    user.Base.metadata.create_all(bind=engine)
    customer.Base.metadata.create_all(bind=engine)
    merchandiser.Base.metadata.create_all(bind=engine)
    product.Base.metadata.create_all(bind=engine)
    product_image.Base.metadata.create_all(bind=engine)
    cart.Base.metadata.create_all(bind=engine)
    cart_item.Base.metadata.create_all(bind=engine)
    address.Base.metadata.create_all(bind=engine)
    credit_card.Base.metadata.create_all(bind=engine)
