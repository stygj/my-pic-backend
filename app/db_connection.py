from dataclasses  import asdict
from contextlib import asynccontextmanager
from typing import Iterator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from app.settings import DBSetting


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DBConnector(metaclass=Singleton):
    """db connect class"""
    def __init__(self, **kwargs) -> None:
        self.DB_HOST: str = kwargs.get("DB_HOST")
        self.DB_PORT: str = kwargs.get("DB_PORT")
        self.DB_USER: str = kwargs.get("DB_USER")
        self.DB_PASSWORD: str = kwargs.get("DB_PASSWORD")
        self.DB_NAME: str = kwargs.get("DB_NAME")
        self.engine: AsyncSession = None

    @asynccontextmanager
    async def get_session(self) -> Iterator[AsyncSession]:
        """get db session"""
        if self.engine is None:
            connection = "postgresql+asyncpg://{}:{}@{}:{}/{}".format(
                self.DB_USER,
                self.DB_PASSWORD,
                self.DB_HOST,
                self.DB_PORT,
                self.DB_NAME
                )
            self.engine = create_async_engine(connection, echo=True)
        session: AsyncSession = AsyncSession(self.engine)
        try:
            yield session
        finally:
            await session.close()


# db 연동
conn = DBConnector(**asdict(DBSetting()))