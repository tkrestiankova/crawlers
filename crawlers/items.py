# items.py

import json
import scrapy
import time

from . import settings
from .database import queries


class Profile(scrapy.Item):
    name = scrapy.Field()
    phone = scrapy.Field()
    website = scrapy.Field()

    def save(self) -> None:
        """
            Save profile into local DB
        """
        if settings.is_prod_env():
            queries.instert_profile(profile=(
                self["name"],
                self["phone"],
                self["website"],
            ))
        else:
            ts = repr(time.time())[:10]
            with open(f"crawlers/results/{ts}.json", "w+") as new_file:
                new_file.write(json.dumps(dict(self)))
