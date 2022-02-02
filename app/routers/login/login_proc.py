import bcrypt
from fastapi import Depends
from fastapi.responses import PlainTextResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Field
from sqlalchemy.sql import select
from app.db.models import User
from app.db.connector import conn




async def login_proc(user: OAuth2PasswordRequestForm = Depends()):
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