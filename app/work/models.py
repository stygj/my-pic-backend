from datetime import datetime
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime)
    deleted: Mapped[DateTime] = mapped_column(DateTime)


class Work(Base):
    __tablename__ = "works"
    __table_args__ = {"schema": "public", "comment": "work table"}
    
    work: Mapped[str] = mapped_column(String(30))
    image_url: Mapped[str] = mapped_column(String(255))
