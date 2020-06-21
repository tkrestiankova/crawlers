# utils.py

import datetime
import re

from .settings import CLIOptions


def yelp_tld(url: str) -> str:
    """
        Determine Yelp tld
    """
    tld_pattern = "^.*www\.yelp\.(.*?)\/.*$"
    if re.search(tld_pattern, url):
        return re.search(tld_pattern, url).group(1)


def cli_help() -> str:
    """
        CLI help string
    """
    _options = ', '.join([opt.value for opt in CLIOptions])
    return (
        "Please provide at least one of the following options: \n"
        f"{_options}.\n"
        "For mor information use --help option"
    )


def alchemy_to_dict(
    model: object,
) -> dict:
    """
        Convert SQLAlchemy model to dictionary.
    """
    dictionary = {}
    for key in model.__table__.columns.keys():
        if hasattr(model, key):
            value = getattr(model, key)
            if isinstance(value, datetime.date):
                value = value.isoformat()
            dictionary[key] = value
    return dictionary
