import os
import asyncio
from typing import List
import uuid

from fastapi import UploadFile
from fastapi_pagination import Page
import aiofiles

from app.photo.repositories import get_photos, add_photos
from app.photo.models import Photo
from app.photo.schemas import PhotoRequestSchema, AddPhotoRequestSchema
from app.settings import ImageSetting
from app.work.models import Work
from app.work.repositories import get_works_by_id


async def get_photo_service(param: PhotoRequestSchema) -> Page[Photo]:
    """get photo service"""
    return await get_photos(param)


async def add_work_service(param: AddPhotoRequestSchema) -> None:
    """add photo service"""  
    work_id = param.work_id
    result: Work = await get_works_by_id(work_id)
    work: str = result.first().work
    file_names: List[str] = await asyncio.gather(
                                *[asyncio.ensure_future(
                                    save_photo_image_file(work, image_file)) for image_file in param.image_files]
                            )
    await add_photos(work_id, work, file_names)


async def save_photo_image_file(work: str, image_file: List[UploadFile]) -> str:
    """save new photos"""
    content: bytes = await image_file.read()
    file_name: str = f"{str(uuid.uuid4())}.jpg"
    dir_path = f"{ImageSetting.PHTO_IMAGE_PATH}/{work}"
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
    async with aiofiles.open(
        f"{dir_path}/{file_name}",
        "wb"
        ) as f:
        await f.write(content)
    return file_name