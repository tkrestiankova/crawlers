# utils.py

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
