# main.py

import scrapy.crawler
import scrapy.utils.project
import click

from . import spiders


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
    """
        Run spider for given URL
    """
    process = scrapy.crawler.CrawlerProcess(
        scrapy.utils.project.get_project_settings()
    )
    spider = spiders.yelp.ProfileSpider

    if profile_url is not None:
        process.crawl(spider, url=profile_url)
    elif list_url is not None:
        process.crawl(spider, url=list_url, list_url=True)
    else:
        print(
            "Please provide at least one of the following options: \n"
            "--profile-url, --list-url.\n"
            "For mor information use --help option"
        )
        return
    process.start()


if __name__ == "__main__":
    run_yelp_spider()
