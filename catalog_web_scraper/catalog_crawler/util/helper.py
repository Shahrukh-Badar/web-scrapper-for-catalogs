from catalog_web_scraper.catalog_crawler.item.catalog_item import Catalog
from catalog_web_scraper.catalog_crawler.item_loader.catalog_item_loader import CatalogLoader
import catalog_web_scraper.catalog_crawler.util.constants as constant


def fill_catalog_item_loader(catalog):
    catalog_item_loader = CatalogLoader(item=Catalog())
    catalog_item_loader.add_value(constant.MANUFACTURER, catalog[constant.MANUFACTURER])
    catalog_item_loader.add_value(constant.CATEGORY, catalog[constant.CATEGORY])
    catalog_item_loader.add_value(constant.MODEL, catalog[constant.MODEL])
    catalog_item_loader.add_value(constant.PART, catalog[constant.PART])
    catalog_item_loader.add_value(constant.PART_CATEGORY, catalog[constant.PART])
    return catalog_item_loader
