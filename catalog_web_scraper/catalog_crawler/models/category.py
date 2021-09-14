from catalog_web_scraper.catalog_crawler.models.abstract import AbstractObject


class Category(AbstractObject):
    def __init__(self, category):
        super().__init__(category)
