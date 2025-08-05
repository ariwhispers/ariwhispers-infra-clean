import functools
from functools import lru_cache
from typing import Literal
from pydantic import AnyUrl, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    ENV: Literal['dev','staging','prod'] = Field('dev', frozen=True)
    LLM_URL: AnyUrl
    IMG_URL: AnyUrl
    VOICE_URL: AnyUrl
    ELEVENLABS_API_KEY: str | None = None
    DISCORD_BOT_TOKEN: str | None = None
    REDIS_URL: AnyUrl = 'redis://redis:6379/0'
    LOG_LEVEL: str = 'INFO'
    model_config = SettingsConfigDict(env_file='.env', case_sensitive=True)
@lru_cache
def get_settings() -> Settings:      # noqa: D401
    return Settings()  # type: ignore[call-arg]
