from pydantic import BaseSettings


class Config(BaseSettings):
    AXIS_API_URL: str = "https://admin-api.axissecurity.com"
    AXIS_API_TOKEN: str = "Not set"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Config()
