from catalog_web_scraper.catalog_crawler.models.abstract import AbstractObject


class Manufacturer(AbstractObject):
    def __init__(self, manufacturer):
        super().__init__(manufacturer)
