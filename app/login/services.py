from typing import Annotated, Dict, Any
from datetime import datetime, timedelta
import jwt

import bcrypt
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from app.login.repositories import get_users
from app.login.models import User
from app.custom_exceptions import AuthenticationException
from app.settings import JWTSetting
from app.login.enums import JWTokenStatus


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def login_service(user: OAuth2PasswordRequestForm) -> Dict[str, Any]:
    """login service"""
    result: User = await get_users(user)
    if not hasattr(result, "username"):
        return AuthenticationException(detail="Invalid Username or Password")
    if not bcrypt.checkpw(
        user.password.encode('utf-8'),
        result.password.encode('utf-8')
    ):
        return AuthenticationException(detail="Invalid Username or Password")
    return await generate_token({"user": result.username})


async def generate_token(payload) -> Dict[str, Any]:
    """generate jwtoken"""
    expired_at: datetime = datetime.utcnow()+timedelta(seconds=JWTSetting.JWT_EXPIRED_TIME)
    encoded: str = jwt.encode(
            payload,
            JWTSetting.JWT_SECRET_KEY,
            algorithm=JWTSetting.JWT_ENCRYPT_ALGORITHM
            )
    return {
        "token_type": "bearer",
        "access_token": encoded,
        "expired_at": expired_at
    }


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> Dict[str, Any]:
    """get current user of token"""
    return await decode_token(token)


async def decode_token(token: str) -> Dict[str, Any]:
    """decode jwtoken"""
    try:
        payload: dict = jwt.decode(
            token,
            JWTSetting.JWT_SECRET_KEY,
            algorithms=[JWTSetting.JWT_ENCRYPT_ALGORITHM])
        return payload
    except jwt.exceptions.ExpiredSignatureError:
        return AuthenticationException(detail=JWTokenStatus.EXPIRED.value)
    except jwt.exceptions.InvalidSignatureError:
        return AuthenticationException(detail=JWTokenStatus.INVALID_SIGNATURE.value)
    except jwt.exceptions.InvalidAlgorithmError:
        return AuthenticationException(detail=JWTokenStatus.INVALID_ALGORITHME.value)
    except jwt.exceptions.DecodeError:
        return AuthenticationException(detail=JWTokenStatus.DECODE_ERROR.value)