
from typing import List

from app.menu.repositories import get_menus
from app.menu.models import Menu


async def get_menu_service() -> List[Menu]:
    """get menu service"""
    return await get_menus()