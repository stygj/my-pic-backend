import os
import time
from uuid import uuid4

from fastapi import  FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

from app.settings import AppSetting, CookieSetting
from app.login import login_api
from app.menu import menu_api
from app.work import work_api
from app.photo import photo_api 


app = FastAPI(
    version=AppSetting.VERSION,
    title=AppSetting.TITLE,
    description=AppSetting.DESCRIPTION
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_uuid_cookie(request: Request, call_next):
    """set uuid in cookie"""
    if "uuid" not in request.cookies:
        uuid_value: str = str(uuid4())
        response: Response = await call_next(request)
        response.set_cookie(
            "uuid",
            uuid_value,
            samesite=CookieSetting.SAMSITE
        )
        return response
    return await call_next(request)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """check api latency"""
    start_time: time = time.time()
    response: Response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.on_event("startup")
def startup_event():
    """이미지 폴더 생성"""
    if not os.path.exists("images/works"):
        os.makedirs("images/works")
    if not os.path.exists("images/photos"):
        os.makedirs("images/photos")


@app.get("/check")
def check():
    return "success"

app.include_router(
    login_api.router,
    tags=["Login"]
)
app.include_router(
    menu_api.router,
    tags=["Menu"]
)
app.include_router(
    work_api.router,
    tags=["Work"]
)
app.include_router(
    photo_api.router,
    tags=["Work"]
)

