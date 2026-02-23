from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "AI Image Forensics"
    DEBUG: bool = False

    # AWS
    AWS_REGION: str = "eu-north-1"
    S3_BUCKET: str = "ai-forensics-bucket"
    AWS_ACCESS_KEY_ID: Optional[str] = None
    AWS_SECRET_ACCESS_KEY: Optional[str] = None

    # Model
    MODEL_NAME: str = "umm-maybe/AI-image-detector"
    MODEL_CACHE_DIR: str = "/app/model_cache"

    DB_PATH: str = "/app/data/jobs.db"

    class Config:
        env_file = ".env"

settings = Settings()