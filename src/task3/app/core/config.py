from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str


settings = Settings(
    app_name="test_api",
)
