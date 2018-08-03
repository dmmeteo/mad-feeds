# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider
from scrapy.http import FormRequest
from feed_parser.items import ProductItem

class MiaFeedSpider(XMLFeedSpider):
    name = 'mia_feed'
    allowed_domains = ['miabellebaby.com']
    iterator = 'iternodes'
    itertag = 'item'
    namespaces = [('g', 'http://base.google.com/ns/1.0')]

    def __init__(self):
        self.url = 'https://www.miabellebaby.com/a/feed/v2/facebook.rss?limit=50&page=%s'
        self.start_urls = [self.url % 1]

    def parse(self, response):
        pages = ''
        data = response.xpath('//comment()').extract()
        for d in data:
            if '<!-- Page: 1 of ' in d:
                pages = d.replace('<!-- Page: 1 of ', '')
                pages = pages.replace(' -->', '')

        for next_page in range(1, int(pages)+1):
            yield response.follow(self.url % next_page, self.get_node)

    def get_node(self, response):
        nodes = self._iternodes(response)
        return self.parse_nodes(response, nodes)

    def parse_node(self, response, node):
        item = ProductItem()
        item['product_id'] = node.xpath('//g:id/text()').extract_first()
        item['title'] = node.xpath('//g:title/text()').extract_first()
        item['description'] = node.xpath('//g:description/text()').extract_first()
        return item





