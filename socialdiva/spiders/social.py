import scrapy
from datetime import datetime
from scrapy.loader import ItemLoader
from socialdiva.items import Article
from itemloaders.processors import TakeFirst


class SocialSpider(scrapy.Spider):
    name = 'social'
    allowed_domains = ['socialdiva.ro']
    start_urls = ['https://socialdiva.ro/']

    def parse(self, response):
        links = response.xpath("//h3/a/@href").getall()
        yield from response.follow_all(links, self.parse_article)

    def parse_article(self, response):
        item = ItemLoader(Article(), response)
        item.default_output_processor = TakeFirst()

        title = response.xpath("//h1//text()").get()
        author = response.xpath("//a[@class='author-meta']/text()").get()

        date = response.xpath("//div[@class='eskimo-date-meta']/text()").get().strip()
        date_time_obj = datetime.strptime(date, '%B %d, %Y')
        date = date_time_obj.strftime("%Y/%m/%d")

        categories = response.xpath("//div[@class='eskimo-cat-meta']/a/text()").getall()
        categories = ", ".join(categories)

        content = response.xpath("//div[@class='eskimo-page-content']/p/text()").getall()
        content = ''.join(content)

        item.add_value("title", title)
        item.add_value("author", author)
        item.add_value("date", date)
        item.add_value("categories", categories)
        item.add_value("content", content)
        item.add_value("link", response.url)

        return item.load_item()
