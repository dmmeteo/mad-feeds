# -*- coding: utf-8 -*-
import scrapy


class MiaFeedSpider(scrapy.Spider):
    name = 'mia_feed'
    allowed_domains = ['miabellebaby.com']

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
            yield response.follow(self.url % next_page, self.parse_item)

    def parse_item(self, response):
        for r in response.css('item'):
            yield {
                'id': r.css('g\:id::text').extract_first(),
                'title': r.css('g\:title::text').extract_first(),
                'url': r.css('g\:link::text').extract_first(),
            }