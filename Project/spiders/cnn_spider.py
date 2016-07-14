# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request

from Project.items import CnnItem


class CnnSpider(CrawlSpider):
    name = 'cnn_spider'
    allowed_domains = ['cnn.com']
    start_urls = ['http://www.cnn.com/']

    rules = (
        Rule(LxmlLinkExtractor(allow=''), callback='parse_item', follow=True),
    )

    def parse_url_start(self, response):
        print("*************************")
        requests = []
        for url in self.start_urls:
            requests.append(Request(url, callback=self.parse_item))
        return requests

    def parse_item(self, response):
        cnn_item = CnnItem()
        cnn_item["title"] = response.xpath('//title/text()').extract()
        cnn_item["links"] = LxmlLinkExtractor(allow=self.allowed_domains,deny=(),unique=True).extract_links(response)

        return cnn_item
