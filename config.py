from dataclasses import dataclass


@dataclass
class AppConfig:
    version: str = "v0.1"
    prefix: str = "user"
    title: str = "user"
    description: str = "this is user api"

@dataclass
class DBConfig:
    driver:str = 'mysql+aiomysql'
    host: str = 'localhost'
    port: int = 0
    user: str =''
    password: str = ''
    db: str = ''