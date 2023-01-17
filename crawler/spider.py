import scrapy
from crawler.innertext import innertext

class TestSpider(scrapy.Spider):
    name = 'test'
    start_urls = ['http://localhost:8999/test.html']
    custom_settings = {
        "FEEDS": {"output/test.json": {"format": "json", "overwrite": True}}
    }

    def parse(self, response):
        labels = innertext(response.css('#header-column th'))
        values = innertext(response.css('#header-column td'))
        yield dict(zip(labels, values))