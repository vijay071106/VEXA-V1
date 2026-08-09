import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = "VEXA"
    APP_VERSION = "1.0.0"

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


settings = Settings()