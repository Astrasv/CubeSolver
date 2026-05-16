from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = "Cube Solver API"
    api_prefix: str = ""
    frontend_origin: str = "http://localhost:5173"


settings = Settings()
