from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, Field
from .login_proc import login_proc


router = APIRouter()


@router.post('/login/')
async def post(user: OAuth2PasswordRequestForm = Depends(login_proc)):
    '''로그인 api입니다.'''
    return user

