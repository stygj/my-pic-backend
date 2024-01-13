from datetime import datetime
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime)
    deleted: Mapped[DateTime] = mapped_column(DateTime)


class Photo(Base):
    __tablename__ = "photos"
    __table_args__ = {"schema": "public", "comment": "photo table"}
    
    image_url: Mapped[str] = mapped_column(String(255))
    work_id: Mapped[int] = mapped_column(Integer)
