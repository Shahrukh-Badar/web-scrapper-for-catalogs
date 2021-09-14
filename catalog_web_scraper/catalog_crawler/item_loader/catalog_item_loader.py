from itemloaders.processors import TakeFirst, MapCompose, Join
from scrapy.loader import ItemLoader


def extract_part(value):
    return value.split('-')[0].strip()


def extract_part_category(value):
    return value.split('-')[1].strip() if len(value.split('-')) > 1 else value.split('-')[0].strip()


class CatalogLoader(ItemLoader):
    default_input_processor = MapCompose(str.strip)
    default_output_processor = TakeFirst()

    part_in = MapCompose(str.strip, extract_part)
    part_category_in = MapCompose(str.strip, extract_part_category)
