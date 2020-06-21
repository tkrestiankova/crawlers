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

    def _exists(self) -> bool:
        """
            Determine if profile already exists
        """
        existing_profiles = queries.profiles_get()
        if any([ep["name"] == self["name"] for ep in existing_profiles]):
            return True
        return False

    def save(self) -> None:
        """
            Save Yelp profile
        """
        if settings.is_prod_env():
            if not self._exists():
                queries.profiles_add(profile={
                    "name": self["name"],
                    "phone": self["phone"],
                    "website": self["website"]
                })
            else:
                queries.profiles_update(profile={
                    "name": self["name"],
                    "phone": self["phone"],
                    "website": self["website"]
                })
        else:
            ts = repr(time.time())[:10]
            with open(f"crawlers/results/{ts}.json", "w+") as new_file:
                new_file.write(json.dumps(dict(self)))
