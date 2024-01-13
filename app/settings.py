import os
from dataclasses import dataclass, field

from dotenv import load_dotenv


load_dotenv()


@dataclass
class AppSetting:
    """Api Setting"""
    VERSION: str = field(default="v0.0.1")
    TITLE: str = field(default="MY-PIC API")
    DESCRIPTION: str = field(default="MY-PIC API")


@dataclass
class DBSetting:
    """DB Connect Setting"""
    DB_HOST: str = field(default=os.environ.get("DB_HOST"))
    DB_PORT: int = field(default=int(os.environ.get("DB_PORT")))
    DB_USER: str = field(default=os.environ.get("DB_USER"))
    DB_PASSWORD: str = field(default=os.environ.get("DB_PASSWORD"))
    DB_NAME: str = field(default=os.environ.get("DB_NAME"))


@dataclass
class CookieSetting:
    """Set Cookie Setting"""
    SAMSITE: str = "lax"
    DOMAIN: str = "roamfocusing.com"


@dataclass
class JWTSetting:
    """Set JWT Setting"""
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
    JWT_ENCRYPT_ALGORITHM = os.environ.get("JWT_ENCRYPT_ALGORITHM")
    JWT_EXPIRED_TIME = int(os.environ.get("JWT_EXPIRED_TIME"))*60*60*24


@dataclass
class ImageSetting:
    """Set images"""
    WORK_IMAGE_PATH = "images/works"
    PHTO_IMAGE_PATH = "images/photos"
    IMAGE_URL = os.environ.get("IMAGE_URL")
    
    