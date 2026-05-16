from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = "Cube Solver API"
    api_prefix: str = ""


settings = Settings()
