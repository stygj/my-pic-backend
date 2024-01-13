from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.login.services import login_service, get_current_user


router = APIRouter()


@router.post(
    "/login",
    description="login"
)
async def post(user: OAuth2PasswordRequestForm = Depends()):
    """로그인 api입니다."""
    return await login_service(user)


@router.get("/users/me")
async def read_users_me(current_user: Annotated[str, Depends(get_current_user)]):
    return current_user
