import pytest
from scrapy.http import Response
import catalog_web_scraper.catalog_crawler.util.constants as constant


@pytest.fixture
def mock_manufacture_response():
    mock_file_path = constant.MOCK_MANUFACTURE_FILE
    file_content = open(mock_file_path, 'r').read().encode('ascii')
    mock_response = Response(url='mock_url',
                             request=None,
                             body=file_content)
    mock_response.encoding = 'utf-8'
    return mock_response
