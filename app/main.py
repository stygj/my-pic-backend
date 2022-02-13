from dataclasses import asdict
from fastapi import  FastAPI
from config import AppConfig, DBConfig
from .routers.register import regist_api
from .routers.login import login_api

# app 객체 생성
app = FastAPI(**asdict(AppConfig()))

app.include_router(regist_api.router)
app.include_router(login_api.router)
