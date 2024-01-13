from datetime import datetime
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime)
    deleted_at: Mapped[DateTime] = mapped_column(DateTime)


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "public", "comment": "user table"}
       
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(15))
    password: Mapped[str] = mapped_column(String(50))
