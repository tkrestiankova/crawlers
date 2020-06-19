# yelp_us.py

from . import yelp


class PTProfileSpider(yelp.ProfileSpider):
    """
        Profile scraper for Portuguese website
    """
    name = "pt_profile_spider"
    allowed_domains = ["yelp.pt"]
    tld = "pt"
