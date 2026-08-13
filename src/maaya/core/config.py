from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Validated application configuration loaded from the environment."""

    app_name: str = "MAAYA Platform"
    environment: Literal["development", "test", "staging", "production"] = "development"
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"
    db_user: str
    db_password: str
    db_name: str
    db_host: str = "127.0.0.1"
    db_port: int = 5432

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="MAAYA_",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Return a cached settings instance for the current process."""
    return Settings()  # pyright: ignore[reportCallIssue]
