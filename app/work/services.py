import uuid
from fastapi import UploadFile
from fastapi_pagination import Page
import aiofiles

from app.work.repositories import get_works, add_work
from app.work.models import Work
from app.work.schemas import AddWorkRequestSchema
from app.settings import ImageSetting


async def get_work_service() -> Page[Work]:
    """get work service"""
    return await get_works()


async def add_work_service(param: AddWorkRequestSchema):
    """add work service"""
    file_name: str = await save_work_image_file(param.image_file)
    await add_work(param.work, file_name)
    

async def save_work_image_file(image_file: UploadFile) -> str:
    """save work image"""
    content: bytes = await image_file.read()
    file_name: str = str(uuid.uuid4())
    async with aiofiles.open(
        f"{ImageSetting.WORK_IMAGE_PATH}/{file_name}.jpg",
        "wb"
        ) as f:
        await f.write(content)
    return file_name
