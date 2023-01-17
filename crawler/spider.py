import scrapy
from crawler.innertext import innertext, innertext_quick

class TestSpider(scrapy.Spider):
    name = 'test'
    start_urls = ['http://localhost:8999/test.html']
    custom_settings = {
        "FEEDS": {"output/test.json": {"format": "json", "overwrite": True}}
    }

    def parse(self, response):
        labels = innertext_quick(response.css('#header-column th'))
        values = innertext_quick(response.css('#header-column td'))
        yield {
            'table': dict(zip(labels, values)),
            'complexText': {
                'innertext_quick': innertext_quick(response.css('#complex-text')),
                'innertext': innertext(response.css('#complex-text'))
            }
        }