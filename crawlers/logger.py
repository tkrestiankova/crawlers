# logger.py

import structlog

def get_logger(module_name: str):
    logger = structlog.get_logger(module_name)
    return logger
