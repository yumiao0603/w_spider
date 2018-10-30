from scrapy.spider import Spider


class IndexSpider(Spider):

    def start_requests(self):
        url = ''