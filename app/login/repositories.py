from typing import List

from sqlalchemy.sql import select
from fastapi.security import OAuth2PasswordRequestForm

from app.db_connection import conn
from app.login.models import User


async def get_users(user: OAuth2PasswordRequestForm) -> User:
    """select menu from db"""
    async with conn.get_session() as session:
        query = select(
                    User.username,
                    User.password
                ).where(
                    User.username == user.username
                )
        result = await session.execute(query)
        return result.first()
   
