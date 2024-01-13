from typing import List

from sqlalchemy.sql import select
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate

from app.db_connection import conn
from app.photo.models import Photo
from app.work.models import Work
from app.photo.schemas import PhotoRequestSchema
from app.settings import ImageSetting


async def get_photos(param: PhotoRequestSchema) -> Page[Photo]:
    """select photos from db"""
    async with conn.get_session() as session:
        query = select(
                    Photo.image_url,
                    Photo.work_id,
                    Work.id
                ).join(
                    Photo, Photo.work_id == Work.id
                ).where(
                    Work.work == param.work
                ).order_by(
                    Photo.id.asc()
                )
        return await paginate(session, query)


async def add_photos(work_id: int, 
                     work: str,
                     file_names: List[str]
                     ) -> None:
    """add new photos"""
    async with conn.get_session() as session:
        async with session.begin():
            session.add_all([
                Photo(
                id=None,
                work_id=work_id,
                image_url=f"{ImageSetting.IMAGE_URL}/{work}/{file_name}.jpg"
                ) for file_name in file_names
            ])