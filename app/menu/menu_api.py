from typing import List

from fastapi import APIRouter, Depends

from app.menu.services import get_menu_service
from app.menu.models import Menu
from app.menu.shemas import MenuResponseSchema


router = APIRouter()


@router.get(
    "/menu",
    description="get menus",
    response_model=List[MenuResponseSchema]
)
async def menu_api(menus: List[Menu] = Depends(get_menu_service)):
    return menus
