from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.base_model import Base


class Work(Base):
    __tablename__ = "works"
    __table_args__ = {"schema": "public", "comment": "work table"}
    
    work: Mapped[str] = mapped_column(String(30))
    image_url: Mapped[str] = mapped_column(String(255))
