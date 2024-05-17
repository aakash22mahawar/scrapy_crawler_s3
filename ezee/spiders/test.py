import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup
import time


class TestSpider(CrawlSpider):
    name = "test"
    allowed_domains = ["franchisesuppliernetwork.com"]
    start_urls = ["https://franchisesuppliernetwork.com/"]

    data = LinkExtractor(allow_domains= allowed_domains)
    rule_data = Rule(data, callback='parse_item', follow=True)
    rules = (rule_data,)

    def parse_item(self, response):
        soup = BeautifulSoup(response.text,'lxml')
        text_data = soup.find_all(text=True) ## text data ##
        text_data = [x.text.strip() for x in text_data]

        image_urls = [img['src'] for img in soup.find_all('img') if not img['src'].endswith('.svg')]  ## images ##
        # Count the number of images
        num_images = len(image_urls)

        # Count the number of URLs
        num_urls = len(soup.find_all('a',href=True))

        print('+++++ yield item +++++')

        # Yield items containing both text data and image URLs
        yield {
            'url' : response.url,
            'num_images' : num_images,
            'num_urls' : num_urls,
            'text_data': text_data,
            'image_urls': image_urls,

        }



