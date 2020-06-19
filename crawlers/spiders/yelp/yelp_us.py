# yelp_us.py

from . import yelp


class USProfileSpider(yelp.ProfileSpider):
    """
        Profile scraper for US website
    """
    name = "us_profile_spider"
    allowed_domains = ["yelp.com"]
    tld = "com"
