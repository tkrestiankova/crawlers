# items.py

import json
import scrapy
import time

from . import settings
from .database import queries


class Profile(scrapy.Item):
    """
        Yelp profile
    """
    name = scrapy.Field()
    phone = scrapy.Field()
    website = scrapy.Field()

    def save(self) -> None:
        """
            Save Yelp profile
        """
        if settings.is_prod_env():
            queries.profiles_add(profile={
                "name": self["name"],
                "phone": self["phone"],
                "website": self["website"]
            })
        else:
            ts = repr(time.time())[:10]
            with open(f"crawlers/results/{ts}.json", "w+") as new_file:
                new_file.write(json.dumps(dict(self)))
