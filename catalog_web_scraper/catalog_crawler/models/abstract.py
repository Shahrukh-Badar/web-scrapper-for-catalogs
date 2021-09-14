from abc import ABC
import catalog_web_scraper.catalog_crawler.util.constants as constant


class AbstractObject(ABC):
    name: str
    url: str

    def __init__(self, element):
        element = element.find('a')
        self.name = element.text
        self.url = constant.BASE_URL + element.attrs['href']
