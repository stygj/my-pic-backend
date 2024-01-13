from typing import List

from pydantic import Field
from fastapi import UploadFile

from app.base_schema import BaseSchema


class PhotoRequestSchema(BaseSchema):
    """get photo request schema"""
    work: str = Field(default="", description="photo's work name")


class PhotoResponseSchema(BaseSchema):
    """get photo response schema"""
    image_url: str = Field(default="", description="photo image url")
    work_id: int = Field(default="", description="photo's work id")
    
    class Config:
        orm_mode = True


class AddPhotoRequestSchema(BaseSchema):
    """add new work request schema"""
    work_id: int = Field(default=0, description="work id")
    image_files: List[UploadFile] = Field(description="photo image files")


class AddWPhotoResponseSchema(BaseSchema):
    """success add new work response schema"""
    message: str = Field(default="succeses")
