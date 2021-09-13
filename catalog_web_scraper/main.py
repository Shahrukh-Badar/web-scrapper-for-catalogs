from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def start_crawl():
    process = CrawlerProcess(get_project_settings())
    process.crawl('catalog')
    process.start()  # the script will block here until the crawling is finished


if __name__ == "__main__":
    start_crawl()
