from sqlalchemy import Column, Integer, String, Sequence, desc
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(15))
    fullname = Column(String(15))
    password = Column(String(50))
    use_yn = Column(Integer)

    def __init__(self, username, fullname, password, use_yn):
        self.username = username
        self.fullname = fullname
        self.password = password
        self.use_yn = use_yn

    def __repr__(self):
        return f"<User({self.username}, {self.fullname}, {self.password}. {self.use_yn})>" 