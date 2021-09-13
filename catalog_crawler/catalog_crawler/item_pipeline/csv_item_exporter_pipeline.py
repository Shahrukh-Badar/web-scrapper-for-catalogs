from scrapy.exporters import CsvItemExporter
FILE_NAME, FILED_TO_EXPORT = '', ''


class CSVItemExporter:
    # def open_spider(self, spider):
    #     file = open(FILE_NAME, 'w+b')
    #     self.csv_exporter = CsvItemExporter(file)
    #     self.csv_exporter.fields_to_export = FILED_TO_EXPORT
    #     self.csv_exporter.start_exporting()
    #
    # def spider_closed(self, spider):
    #     self.csv_exporter.finish_exporting()

    def process_item(self, item, spider):
        pass
        # self.csv_exporter.export_item(item)
        # return item

