# app/config/settings.py
from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()

@dataclass
class Settings:
    api_key: str = os.getenv("DELTA_API_KEY", "")
    api_secret: str = os.getenv("DELTA_API_SECRET", "")
    base_url: str = os.getenv(
        "BASE_URL",
        "https://api.delta.exchange",
    )
    symbol: str = os.getenv("SYMBOL","BTCUSD")

settings = Settings()