import os

from dotenv import load_dotenv

from logger import get_logger

logger = get_logger()

load_dotenv()
HF_API_KEY=os.getenv("HF_API_KEY")

if not HF_API_KEY:
    logger.error("HF API key not found.Please HF_API_KEY is not set")
    exit(1)

ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")
if not ELEVEN_API_KEY:
    logger.error("API key not found. Please set ELEVEN_API_KEY in .env")
    raise ValueError("Missing ELEVEN_API_KEY")
