# yelp_us.py

from . import yelp


class PTProfileSpider(yelp.ProfileSpider):
    name = "pt_profile_spider"
    allowed_domains = ["yelp.pt"]
    tld = "pt"
