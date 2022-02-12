from dataclasses  import asdict
from config import DBConfig
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DBConnector(metaclass=Singleton):
    def __init__(self, **kwargs):
        self.driver = kwargs.get('driver')
        self.host = kwargs.get('host')
        self.port = kwargs.get('port')
        self.user = kwargs.get('user')
        self.password = kwargs.get('password')
        self.db = kwargs.get('db')
        self.engine = None
        self.session = None

    def get_session(self):

        if self.engine is None:
            connection = '{}://{}:{}@{}:{}/{}'.format(self.driver, self.user, self.password, self.host, self.port, self.db)
            self.engine = create_async_engine(connection, echo=True)
        return scoped_session(sessionmaker(self.engine, autoflush=False, expire_on_commit=False, class_=AsyncSession))

def test_connect():
    # db 연동
    conn = DBConnector(**asdict(DBConfig()))
    engine1 = conn.engine
    engine2 = conn.engine
    session1 = conn.get_session()
    session2 = conn.get_session()
    # 하나의 engine
    assert engine1 == engine2
    # 여러개 session으로 transaction을 관리
    assert session1 != session2
