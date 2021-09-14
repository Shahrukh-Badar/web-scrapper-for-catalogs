from catalog_web_scraper.catalog_crawler.models.abstract import AbstractObject


class Part(AbstractObject):
    def __init__(self, part):
        super().__init__(part)
