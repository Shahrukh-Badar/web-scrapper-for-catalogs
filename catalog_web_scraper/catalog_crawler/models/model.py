from catalog_web_scraper.catalog_crawler.models.abstract import AbstractObject


class Model(AbstractObject):
    def __init__(self, model):
        super().__init__(model)
