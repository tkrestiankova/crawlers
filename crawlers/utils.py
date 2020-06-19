# utils.py

import re

def is_yelp_us_website(url: str) -> bool:
    if re.search("www.yelp.com", url):
        return True
    return False

def is_yelp_pt_website(url: str) -> bool:
    if re.search("www.yelp.pt", url):
        return True
    return False
