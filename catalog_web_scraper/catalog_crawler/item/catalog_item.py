# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Catalog(scrapy.Item):
    manufacturer = scrapy.Field()
    category = scrapy.Field()
    model = scrapy.Field()
    part = scrapy.Field()
    part_category = scrapy.Field()
