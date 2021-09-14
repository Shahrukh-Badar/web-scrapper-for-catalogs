import scrapy
from bs4 import BeautifulSoup
from catalog_web_scraper.catalog_crawler.item.catalog_item import Catalog
from catalog_web_scraper.catalog_crawler.item_loader.catalog_item_loader import CatalogLoader
from catalog_web_scraper.catalog_crawler.models.manufacturer import Manufacturer
from catalog_web_scraper.catalog_crawler.models.category import Category
from catalog_web_scraper.catalog_crawler.models.model import Model
from catalog_web_scraper.catalog_crawler.models.part import Part
import catalog_web_scraper.catalog_crawler.util.constants as constant


class CatalogSpider(scrapy.Spider):
    name = constant.SPIDER_NAME

    def start_requests(self):
        urls = [
            constant.START_URL
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_manufacturer)

    def parse_manufacturer(self, response):
        soup = BeautifulSoup(response.body, constant.PARSER)
        manufacturers = soup.select(constant.MANUFACTURER_SELECTOR)[constant.FIRST_ELEMENT].find(
            constant.UNORDERED_LIST).find_all(
            constant.LIST_ITEM)
        for manufacturer in manufacturers[:1]:
            manufacturer = Manufacturer(manufacturer)
            request = scrapy.Request(url=manufacturer.url, callback=self.parse_categories)
            request.cb_kwargs[constant.MANUFACTURER] = manufacturer.name
            yield request

    def parse_categories(self, response, **kwargs):
        soup = BeautifulSoup(response.body, constant.PARSER)
        categories = soup.select(constant.CATEGORY_SELECTOR)[constant.FIRST_ELEMENT].find(
            constant.UNORDERED_LIST).find_all(
            constant.LIST_ITEM)
        for category in categories:
            category = Category(category)
            request = scrapy.Request(url=category.url, callback=self.parse_models)
            request.cb_kwargs[constant.MANUFACTURER] = kwargs[constant.MANUFACTURER]
            request.cb_kwargs[constant.CATEGORY] = category.name
            yield request

    def parse_models(self, response, **kwargs):
        soup = BeautifulSoup(response.body, constant.PARSER)
        models = soup.select(constant.MODEL_SELECTOR)[constant.FIRST_ELEMENT].find(constant.UNORDERED_LIST).find_all(
            constant.LIST_ITEM)
        for model in models:
            model = Model(model)
            request = scrapy.Request(url=model.url, callback=self.parse_parts)
            request.cb_kwargs[constant.MANUFACTURER] = kwargs[constant.MANUFACTURER]
            request.cb_kwargs[constant.CATEGORY] = kwargs[constant.CATEGORY]
            request.cb_kwargs[constant.MODEL] = model.name
            yield request

    def parse_parts(self, response, **kwargs):
        soup = BeautifulSoup(response.body, constant.PARSER)
        parts = soup.select(constant.PART_SELECTOR)[constant.FIRST_ELEMENT].find(constant.UNORDERED_LIST).find_all(
            constant.LIST_ITEM)
        for part in parts:
            part = Part(part)
            l = CatalogLoader(item=Catalog(), response=response)
            l.add_value(constant.MANUFACTURER, kwargs[constant.MANUFACTURER])
            l.add_value(constant.CATEGORY, kwargs[constant.CATEGORY])
            l.add_value(constant.MODEL, kwargs[constant.MODEL])
            l.add_value(constant.PART, part.name)
            l.add_value(constant.PART_CATEGORY, part.name)
            yield l.load_item()
