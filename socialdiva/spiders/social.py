import scrapy


class SocialSpider(scrapy.Spider):
    name = 'social'
    allowed_domains = ['socialdiva.ro']
    start_urls = ['http://socialdiva.ro/']

    def parse(self, response):
        pass
