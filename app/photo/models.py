from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column


class Base(MappedAsDataclass, DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)


class Photo(Base):
    __tablename__ = "photos"
    __table_args__ = {"schema": "public", "comment": "photo table"}
    
    image_url: Mapped[str] = mapped_column(String(255))
    work_id: Mapped[int] = mapped_column(Integer)
