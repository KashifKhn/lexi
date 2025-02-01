import os
import sys

from loguru import logger

LOG_DIR = "logs"

if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

logger.remove()

logger.add(
        sys.stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
           "<level>{message}</level>",
        colorize=True,
        level="DEBUG"
)

logger.add(
        f"{LOG_DIR}/lexi_logs.log",
        rotation="10MB",
        retention="7 days",
        compression="zip",
        level="INFO", 
        enqueue=True,
        backtrace=True,
        diagnose=True
)

def get_logger() :
    return logger



