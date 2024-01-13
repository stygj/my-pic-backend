from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column


class Base(MappedAsDataclass, DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)


class Work(Base):
    __tablename__ = "works"
    __table_args__ = {"schema": "public", "comment": "work table"}
    
    work: Mapped[str] = mapped_column(String(30))
    image_url: Mapped[str] = mapped_column(String(255))
