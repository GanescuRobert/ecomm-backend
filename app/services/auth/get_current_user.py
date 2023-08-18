from email.header import Header
from fastapi import HTTPException, Security, Depends
import jwt
from app.services.helpers.settings import settings


def _get_authorization_header(authorization: str = Header(None)):
    return authorization


def _get_token_from_header(authorization: str = Depends(_get_authorization_header)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header missing")
    token_type, token = authorization.split()
    if token_type.lower() != "bearer":
        raise HTTPException(status_code=401, detail="Invalid token type")
    return token


def _verify_jwt_token(token: str = Security(_get_token_from_header)):
    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except (jwt.DecodeError, jwt.InvalidTokenError):
        raise HTTPException(status_code=401, detail="Invalid token")


async def get_current_user(token: str = Depends(_verify_jwt_token)):
    return token.get("sub")
