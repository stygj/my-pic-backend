from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.base_model import Base


class Photo(Base):
    __tablename__ = "photos"
    __table_args__ = {"schema": "public", "comment": "photo table"}
    
    image_url: Mapped[str] = mapped_column(String(255))
    work_id: Mapped[int] = mapped_column(Integer)
