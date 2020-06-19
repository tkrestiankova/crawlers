# items.py

import json
import scrapy
import time

from . import settings


class Profile(scrapy.Item):
    name = scrapy.Field()
    phone = scrapy.Field()
    website = scrapy.Field()
    info_source = scrapy.Field()

    def save(self) -> None:
        if settings.is_prod_env():
            return
        else:
            ts = repr(time.time())[:10]
            with open(f"crawlers/results/{ts}.json", "w+") as new_file:
                new_file.write(json.dumps(dict(self)))
