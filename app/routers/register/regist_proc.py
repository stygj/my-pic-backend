import bcrypt
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel, Field
from sqlalchemy.sql import select
from app.db.models import User
from app.db.connector import conn


class UserModel(BaseModel):
    username :str = Field("", title='user name', max_length=15)
    fullname : str = Field("", title="full name", max_length=15)
    password: str = Field("", title="password", max_length=50)


async def check_user(user: User):
    '''username이 db에 존재하는지 확인합니다.'''
    session = conn.get_session()
    async with session() as session:
        result = await session.execute(select(User.username).where(User.username == user.username))
        return True if result.first() else False


async def regist_user(user: User):
    '''새로운 user를 추가합니다.'''
    session = conn.get_session()
    async with session() as session:
        async with session.begin():
            session.add(user)
    await session.close()
    await conn.engine.dispose()


async def regist_proc(user: UserModel):
    '''회원가입 프로세스를 진행합니다'''
    user = User(
            user.username, 
            user.fullname,
            bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode(),
            0
    )
    try:
        check = await check_user(user)
        if not check:
            await regist_user(user)
            return PlainTextResponse("OK", 200)
        else:
            return PlainTextResponse("Aleady exist username", 400)
    except Exception as e:
        print(e)
        return PlainTextResponse("FAIL", 500)

