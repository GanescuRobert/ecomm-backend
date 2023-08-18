from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.models.user import User
from app.database.models.cart import Cart
from app.database.schemas.user import UserLogin, UserRegister
from app.database.session import get_database_session
from app.services.auth.create_jwt_token import create_jwt_token
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/register/")
async def register(user: UserRegister, db: Session = Depends(get_database_session)):
    user_db = db.query(User).filter(User.email == user.email).first()

    if user_db:
        raise HTTPException(status_code=400, detail="User already registered")

    hashed_password = pwd_context.hash(user.password.get_secret_value())

    new_user = User(
        email=user.email,
        hashed_password=hashed_password,
        is_superuser=user.is_superuser,
    )
    db.add(new_user)
    db.commit()

    new_cart = Cart(user=new_user)
    db.add(new_cart)
    db.commit()

    jwt_token = create_jwt_token(new_user.email)

    return {"message": "Registration successful", "token": jwt_token}


@router.post("/login/")
async def login(user_login: UserLogin, db: Session = Depends(get_database_session)):
    user_db = db.query(User).filter(User.email == user_login.email).first()

    if not user_db or not user_db.verify_password(
        user_login.password.get_secret_value()
    ):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    jwt_token = create_jwt_token(user_db.email)

    return {"message": "Login successful", "token": jwt_token}
