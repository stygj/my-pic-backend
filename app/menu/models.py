from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.base_model import Base


class Menu(Base):
    __tablename__ = "menus"
    __table_args__ = {"schema": "public", "comment": "menu table"}
       
    menu_name: Mapped[str] = mapped_column(String(30))
    url_path: Mapped[str] = mapped_column(String(30))
