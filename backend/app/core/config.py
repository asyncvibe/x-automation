from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    twitter_api_key: str
    twitter_api_secret_key: str
    twitter_access_token: str
    twitter_access_token_secret: str

    class Config:
        env_file = ".env"

settings = Settings()