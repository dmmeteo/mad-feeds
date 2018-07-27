# -*- coding: utf-8 -*-
import scrapy


class MiaFeedSpider(scrapy.Spider):
    name = 'mia_feed'
    allowed_domains = ['miabellebaby.com']

    url = 'https://www.miabellebaby.com/a/feed/v2/facebook.rss?limit=50&page=%s'
    page = 1

    def start_requests(self):
        yield scrapy.Request(self.url % self.page, self.parse)

    def parse(self, response):
        if response.css('item'):
            for quote in response.css('item'):
                yield {
                    'id': quote.css('g\:id::text').extract_first(),
                    'title': quote.css('g\:title::text').extract_first(),
                }

            self.page += 1
            next_page = self.url % self.page

            if next_page is not None:
                yield response.follow(next_page, self.parse)
