import logging
from pathlib import Path
from src.config.settings import LOG_DIR
import sys



LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "etl.log"


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout)
    ]
)


logger = logging.getLogger(__name__)