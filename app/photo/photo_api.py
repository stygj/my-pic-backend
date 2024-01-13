from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer
from fastapi_pagination import Page, add_pagination

from app.photo.services import get_photo_service, add_work_service
from app.photo.schemas import (
    PhotoResponseSchema,
    PhotoRequestSchema,
    AddPhotoRequestSchema,
    AddWPhotoResponseSchema
)
from app.login.services import decode_token


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@router.get(
    "/photo",
    description="get photos",
    response_model=Page[PhotoResponseSchema]
)
async def photo_api(param: PhotoRequestSchema = Depends()):
    return await get_photo_service(param)


@router.post(
    "/addPhoto",
    description="add photos"
)
async def add_work_api(
    param: AddPhotoRequestSchema = Depends(),
    token: str = Depends(oauth2_scheme)
    ):
    result = await decode_token(token)
    if not isinstance(result, dict):
        return result
    
    await add_work_service(param)
    return JSONResponse(
        status_code=200,
        content=jsonable_encoder(AddWPhotoResponseSchema()),
        media_type="application/json"
        )


add_pagination(router)
