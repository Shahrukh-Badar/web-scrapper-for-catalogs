import catalog_web_scraper.catalog_crawler.util.constants as constant
from catalog_web_scraper.catalog_crawler.util.parser_helper import ParserHelper


def test_format_data_for_display(mock_manufacture_response):
    data = ParserHelper.parse_helper(mock_manufacture_response, constant.MANUFACTURER_SELECTOR)
    elements_type = data.source.name

    assert elements_type == constant.LIST_ITEM
