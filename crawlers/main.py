# main.py

import scrapy.crawler
import scrapy.utils.project
import click
import re

from . import spiders, utils
from .database import queries


def get_yelp_spider(url: str):
    if utils.is_yelp_us_website(url):
        return spiders.yelp.yelp_us.USProfileSpider
    elif utils.is_yelp_pt_website(url):
        return spiders.yelp.yelp_pt.PTProfileSpider
    else:
        return


@click.command()
@click.option(
    "--profile-url",
    default=None,
    help="Yelp profile for crawling"
)
@click.option(
    "--list-url",
    default=None,
    help="List of yelp profiles for crawling"
)
def run_yelp_spider(profile_url: str = None, list_url: str = None) -> None:

    if all([
        profile_url is None,
        list_url is None
    ]):
        print(
            "Please provide at least one of the following options: \n"
            "--profile-url, --list-url.\n"
            "For mor information use --help option"
        )
        exit()

    from_list = False
    url = None
    spider = None

    if list_url is not None:
        from_list = True
        url = list_url
        spider = get_yelp_spider(list_url)
    else:
        url = profile_url
        spider = get_yelp_spider(profile_url)

    if spider:
        process = scrapy.crawler.CrawlerProcess(
            scrapy.utils.project.get_project_settings()
        )
        process.crawl(spider, url=url, list_url=from_list)
        process.start()
    else:
        print(
            "Please provide Portuguese or US yelp website"
        )
        exit()


if __name__ == "__main__":
    if not queries.create_profiles_table():
        print("Unable to create profiles table")
        exit()
    run_yelp_spider()
