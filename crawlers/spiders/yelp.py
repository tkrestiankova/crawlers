# yelp.py

from lxml import html
import random
import re
import requests
import scrapy
from typing import List

from .. import items
from ..user_agents import USER_AGENTS
from ..proxies import PROXIES
from . import yelp_constants as const

URL = "https://www.yelp.com"

class ProfileSpider(scrapy.spiders.crawl.CrawlSpider):
    name = "profile_spider"

    def __init__(self, url: str, list_url: bool = False):
        """
            Either init spider with profile url or
            with url containing links to profiles
        """
        self.url = url
        self.list_url = list_url

    def parse_profile_url(self, response):
        """
            parse url paths to profiles, this will only work for
            the first page. To process all pages it would be necessary
            to iterate over pages (parameter start)
        """
        params = response.xpath(
            f"//ul[@class='{const.list_url_ul_cls}']/li"
            f"[@class='{const.list_url_li_cls}']//"
            f"a[@class='{const.list_url_a_cls}']/@href"
        )
        for param in params:
            yield scrapy.Request(
                f"{URL}{param}",
                callback=self.parse
            )

    def elem(self, cls: str) -> str:
        return re.search('^lemon--(.*?)__', cls).group(1)

    def parent(self, cls: str):
        elem = self.elem(cls=cls)
        return self.response.xpath(f"//{elem}[@class='{cls}']")

    def value(self, cls: str, parent = None) -> str:
        elem = self.elem(cls=cls)
        if parent is None:
            parent = self.response
        return parent.xpath(f".//{elem}[@class='{cls}']/text()").get()

    def start_requests(self):
        if self.list_url:
            yield scrapy.Request(
                self.url,
                callback=self.parse_profile_url,
                # headers={'User-Agent': random.choice(USER_AGENTS)},
                # meta={'proxy': random.choice(PROXIES)}
            )
        else:
            yield scrapy.Request(
                self.url,
                callback=self.parse,
                # headers={'User-Agent': random.choice(USER_AGENTS)},
                # meta={'proxy': random.choice(PROXIES)}
            )

    def parse(self, response):
        self.response = response
        contact_info = self.parent(cls=const.contact_info_cls)
        profile = items.Profile(
            name=self.value(cls=const.name_cls),
            phone=self.value(cls=const.phone_cls, parent=contact_info),
            website=self.value(cls=const.web_cls, parent=contact_info)
        )
        profile.save()
