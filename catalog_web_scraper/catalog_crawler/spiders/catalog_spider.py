import scrapy
from bs4 import BeautifulSoup
from catalog_web_scraper.catalog_crawler.models.manufacturer import Manufacturer
from catalog_web_scraper.catalog_crawler.models.category import Category
from catalog_web_scraper.catalog_crawler.models.model import Model
from catalog_web_scraper.catalog_crawler.models.part import Part
import catalog_web_scraper.catalog_crawler.util.constants as constant
from catalog_web_scraper.catalog_crawler.util.parser_helper import ParserHelper
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError


class CatalogSpider(scrapy.Spider):
    name = constant.SPIDER_NAME

    def start_requests(self):
        urls = [
            constant.START_URL
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_manufacturer, errback=self.errback_httpbin)

    def parse_manufacturer(self, response):
        manufacturers = ParserHelper.parse_helper(response, constant.MANUFACTURER_SELECTOR)
        for manufacturer in manufacturers[:1]:
            manufacturer = Manufacturer(manufacturer)
            request = scrapy.Request(url=manufacturer.url, callback=self.parse_categories, errback=self.errback_httpbin)
            request.cb_kwargs[constant.MANUFACTURER] = manufacturer.name
            yield request

    def parse_categories(self, response, **kwargs):
        categories = ParserHelper.parse_helper(response, constant.CATEGORY_SELECTOR)
        for category in categories:
            category = Category(category)
            request = scrapy.Request(url=category.url, callback=self.parse_models, errback=self.errback_httpbin)
            request.cb_kwargs[constant.MANUFACTURER] = kwargs[constant.MANUFACTURER]
            request.cb_kwargs[constant.CATEGORY] = category.name
            yield request

    def parse_models(self, response, **kwargs):
        models = ParserHelper.parse_helper(response, constant.MODEL_SELECTOR)
        for model in models:
            model = Model(model)
            request = scrapy.Request(url=model.url, callback=self.parse_parts, errback=self.errback_httpbin)
            request.cb_kwargs[constant.MANUFACTURER] = kwargs[constant.MANUFACTURER]
            request.cb_kwargs[constant.CATEGORY] = kwargs[constant.CATEGORY]
            request.cb_kwargs[constant.MODEL] = model.name
            yield request

    def parse_parts(self, response, **kwargs):
        parts = ParserHelper.parse_helper(response, constant.PART_SELECTOR)
        for part in parts:
            part = Part(part)
            kwargs[constant.PART] = part.name
            yield ParserHelper.fill_catalog_item_loader(kwargs).load_item()

    def errback_httpbin(self, failure):
        # log all errback failures,
        # in case you want to do something special for some errors,
        # you may need the failure's type
        self.logger.error(repr(failure))

        # if isinstance(failure.value, HttpError):
        if failure.check(HttpError):
            # you can get the response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)

        # elif isinstance(failure.value, DNSLookupError):
        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        # elif isinstance(failure.value, TimeoutError):
        elif failure.check(TimeoutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)

# https://stackoverflow.com/questions/31146046/how-do-i-catch-errors-with-scrapy-so-i-can-do-something-when-i-get-user-timeout
# https://stackoverflow.com/questions/54802529/how-can-i-get-the-original-request-url-in-errback-using-scrapy
