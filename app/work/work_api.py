from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer
from fastapi_pagination import Page, add_pagination

from app.work.services import get_work_service, add_work_service
from app.work.schemas import WorkResponseSchema, AddWorkRequestSchema, AddWorkResponseSchema
from app.login.services import decode_token


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@router.get(
    "/work",
    description="get works",
    response_model=Page[WorkResponseSchema]
)
async def work_api(result: Page[WorkResponseSchema] = Depends(get_work_service)):
    return result


@router.post(
    "/addWork",
    description="add works"
)
async def add_work_api(
    param: AddWorkRequestSchema = Depends(),
    token: str = Depends(oauth2_scheme)
    ):
    result = await decode_token(token)
    if not isinstance(result, dict):
        return result
    
    await add_work_service(param)
    return JSONResponse(
        status_code=200,
        content=jsonable_encoder(AddWorkResponseSchema()),
        media_type="application/json"
        )



add_pagination(router)
