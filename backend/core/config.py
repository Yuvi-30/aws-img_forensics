from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "AI Image Forensics"
    DEBUG: bool = False

    # AWS
    AWS_REGION: str = "us-east-1"
    S3_BUCKET: str = "ai-forensics-bucket"

    # Model
    MODEL_NAME: str = "umm-maybe/AI-image-detector"
    MODEL_CACHE_DIR: str = "/app/model_cache"

    # DB
    DB_PATH: str = "/app/data/jobs.db"

    class Config:
        env_file = ".env"

settings = Settings()
