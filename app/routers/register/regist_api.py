from fastapi import APIRouter, Depends
from .regist_proc import UserModel, regist_proc

router = APIRouter()

@router.post('/register/')
async def post(user: UserModel = Depends(regist_proc)):
    '''회원가입 api입니다.'''
    return user
