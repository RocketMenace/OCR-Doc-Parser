from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="allow"
    )
    ENV_STATE: str | None = None


class DevConfig(BaseConfig):
    model_config = SettingsConfigDict(env_prefix="DEV_")
    BASE_FILES_DIR: str = "app/files"
    MISTRAL_API_KEY: str | None


config = DevConfig()
