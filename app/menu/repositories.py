from typing import List

from sqlalchemy.sql import select

from app.db_connection import conn
from app.menu.models import Menu


async def get_menus() -> List[Menu]:
    """select menu from db"""
    async with conn.get_session() as session:
        query = select(
                    Menu.id,
                    Menu.menu_name,
                    Menu.url_path
                ).order_by(
                    Menu.id.asc()
                )
        return await session.execute(query)
