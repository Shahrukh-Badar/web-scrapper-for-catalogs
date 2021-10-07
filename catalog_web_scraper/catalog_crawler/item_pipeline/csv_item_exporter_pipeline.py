from datetime import date
import catalog_web_scraper.catalog_crawler.util.constants as constant
from scrapy.exporters import CsvItemExporter


class CSVItemExporter:
    def open_spider(self, spider):
        file_name = f'./storage/output/{str(date.today())}_{constant.OUTPUT_FILE_NAME}'
        file = open(file_name, 'w+b')
        self.csv_exporter = CsvItemExporter(file)
        self.csv_exporter.fields_to_export = [constant.MANUFACTURER, constant.CATEGORY, constant.MODEL, constant.PART,
                                              constant.PART_CATEGORY]
        self.csv_exporter.start_exporting()

    def spider_closed(self, spider):
        self.csv_exporter.finish_exporting()

    def process_item(self, item, spider):
        self.csv_exporter.export_item(item)
        return item
