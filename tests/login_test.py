import bcrypt
from dataclasses  import asdict
from fastapi import Depends
from fastapi.responses import PlainTextResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.sql import select
from config import DBConfig
from connector_test import DBConnector
from models import User

async def login_proc(user):
    conn = DBConnector(**asdict(DBConfig()))
    session = conn.get_session()
    async with session() as session:
        result = await session.execute(select(User.username, User.password).where(User.username == user.username))
        user_info = result.fetchall()

        byte_pw = None
        check_pw = False
        response_data = PlainTextResponse("LOGIN FAIL", 400)
        if len(user_info) > 0:
            byte_pw = user_info[0][1]
        if byte_pw:
            check_pw = bcrypt.checkpw(user.password.encode('utf-8'), byte_pw.encode('utf-8'))
        if check_pw:
            response_data = {"username" : user.username}
        return response_data


conn = None

def test_login(get_session):
    global conn
    conn = get_session

    import asyncio

    class OAuth2PasswordRequestForm:
        username: str
        password: str

    user = OAuth2PasswordRequestForm()
    user.username = "admin"
    user.password = "admin"
    result = asyncio.run(login_proc(user))
    print(result)
    