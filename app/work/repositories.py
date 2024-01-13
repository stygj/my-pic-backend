from sqlalchemy.sql import select
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate

from app.db_connection import conn
from app.work.models import Work
from app.settings import ImageSetting


async def get_works() -> Page[Work]:
    """select works from db"""
    async with conn.get_session() as session:
        query = select(
                    Work.work,
                    Work.image_url
                ).order_by(
                    Work.id.desc()
                )
        return await paginate(session, query)


async def get_works_by_id(work_id: int) -> Page[Work]:
    """select works from db"""
    async with conn.get_session() as session:
        query = select(
                    Work.work
                ).where(
                    Work.id == work_id
                )
        return await session.execute(query)


async def add_work(work: str, file_name: str) -> None:
    """add new work"""
    async with conn.get_session() as session:
        async with session.begin():
            session.add(Work(
                id=None,
                work=work,
                image_url=f"{ImageSetting.IMAGE_URL}/{work}/{file_name}.jpg"
            ))
