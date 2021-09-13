from itemloaders.processors import TakeFirst, MapCompose, Join
from scrapy.loader import ItemLoader


class CatalogLoader(ItemLoader):
    default_input_processor = MapCompose(str.strip)
    default_output_processor = TakeFirst()

