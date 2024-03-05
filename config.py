import multiprocessing

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    port: Optional[int] = 8000
    workers: Optional[int] = multiprocessing.cpu_count()

    model_config = SettingsConfigDict(env_file=".env", extra="allow")


settings = Settings()
