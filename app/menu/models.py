from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column


class Base(MappedAsDataclass, DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)


class Menu(Base):
    __tablename__ = "menus"
    __table_args__ = {"schema": "public", "comment": "menu table"}
       
    menu_name: Mapped[str] = mapped_column(String(30))
    url_path: Mapped[str] = mapped_column(String(30))
