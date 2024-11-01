from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class DBConfig(BaseModel):
    url: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="../.env",
        env_nested_delimiter="__",
        case_sensitive=False,
        extra="ignore"
    )

    db: DBConfig


settings = Settings()
