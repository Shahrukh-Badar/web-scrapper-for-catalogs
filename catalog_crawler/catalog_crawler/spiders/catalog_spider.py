import scrapy
from bs4 import BeautifulSoup, Tag


class CatalogSpider(scrapy.Spider):
    name = "catalog"
    base_url = 'https://www.urparts.com/'

    def start_requests(self):
        urls = [
            f'{self.base_url}index.cfm/page/catalogue'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_makes)

    def parse_makes(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        makes = soup.select("div.c_container.allmakes")[0].find('ul').find_all('li')
        for make in makes[:1]:
            make = make.find('a')
            make_name = make.text
            make_url = make.attrs['href']
            category_url = f'{self.base_url}{make_url}'
            request = scrapy.Request(url=category_url, callback=self.parse_categories)
            request.cb_kwargs['make'] = make_name
            yield request

    def parse_categories(self, response, **kwargs):
        soup = BeautifulSoup(response.body, 'html.parser')
        categories = soup.select("div.c_container.allmakes.allcategories")[0].find('ul').find_all('li')
        for category in categories[:1]:
            category = category.find('a')
            category_name = category.text
            category_url = category.attrs['href']
            model_url = f'{self.base_url}{category_url}'
            request = scrapy.Request(url=model_url, callback=self.parse_models)
            request.cb_kwargs['make'] = kwargs['make']
            request.cb_kwargs['category'] = category_name
            yield request

    def parse_models(self, response, **kwargs):
        soup = BeautifulSoup(response.body, 'html.parser')
        models = soup.select("div.c_container.allmodels")[0].find('ul').find_all('li')
        for model in models[:1]:
            model = model.find('a')
            model_name = model.text
            model_url = model.attrs['href']
            part_url = f'{self.base_url}{model_url}'
            request = scrapy.Request(url=part_url, callback=self.parse_parts)
            request.cb_kwargs['make'] = kwargs['make']
            request.cb_kwargs['category'] = kwargs['category']
            request.cb_kwargs['model'] = model_name
            yield request

    def parse_parts(self, response, **kwargs):
        soup = BeautifulSoup(response.body, 'html.parser')
        parts = soup.select("div.c_container.allparts")[0].find('ul').find_all('li')
        for part in parts[:1]:
            part = part.find('a')
            part_name = part.text
            part_url = part.attrs['href']

