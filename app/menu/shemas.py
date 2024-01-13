from pydantic import Field
from app.base_schema import BaseSchema


class MenuResponseSchema(BaseSchema):
    """menu response model"""
    id: int = Field(default=0, description="menu id")
    menu_name: str = Field(default="", description="menu name")
    url_path: str = Field(default="", description="url path")
    
    class Config:
        orm_mode = True
