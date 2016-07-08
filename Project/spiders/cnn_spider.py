# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.items import CnnItem


class CnnSpider(CrawlSpider):
    name = 'cnn_spider'
    allowed_domains = ['cnn.com']
    start_urls = ['http://www.cnn.com/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        cnn_item = CnnItem()
        cnn_item["title"] = response.xpath('//title/text()').extract()
        cnn_item["links"] = response.xpath('//a[@href]/@href').extract()
        return cnn_item
