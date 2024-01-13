from pydantic import Field
from fastapi import UploadFile

from app.base_schema import BaseSchema


class WorkResponseSchema(BaseSchema):
    """get works response schema"""
    work: str = Field(default=4, description="work name")
    image_url: str = Field(default="", description="work thumbnail image url")
    
    class Config:
        orm_mode = True


class AddWorkRequestSchema(BaseSchema):
    """add new work request schema"""
    work: str = Field(default="", description="work name")
    image_file: UploadFile = Field(description="work thumbnail images")


class AddWorkResponseSchema(BaseSchema):
    """success add new work response schema"""
    message: str = Field(default="succeses")