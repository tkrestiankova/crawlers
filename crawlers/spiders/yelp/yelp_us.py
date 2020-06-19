# yelp_us.py

from . import yelp


class USProfileSpider(yelp.ProfileSpider):
    name = "us_profile_spider"
    allowed_domains = ["yelp.com"]
    tld = "com"
