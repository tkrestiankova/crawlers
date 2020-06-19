# settings.py

import os

from .logger import get_logger

log = get_logger(__name__)


def load_variable(name: str, default: str = None) -> str:
    variable = os.environ.get(name, default)
    if not variable:
        log.error(f"Unable to load variable {name}")
    return variable


ENVIRONMENT = load_variable("ENVIRONMENT", "production")

def is_prod_env() -> bool:
    return ENVIRONMENT == "production"

def is_local_env() -> bool:
    return ENVIRONMENT == "local"

DB_NAME = "crawlers.db"

# Scrapy settings
BOT_NAME = "crawlers"

SPIDER_MODULES = ["crawlers.spiders"]
NEWSPIDER_MODULE = "crawlers.spiders"
ROBOTSTXT_OBEY = False

RETRY_TIMES = 5
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
