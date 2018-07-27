# -*- coding: utf-8 -*-
import scrapy


class MiaHTMLSpider(scrapy.Spider):
    name = 'mia_html'
    allowed_domains = ['miabellebaby.com']

    def start_requests(self):
        # TODO select urls from mongodb/redis
        urls = ['']
        for url in urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        # TODO yield meta tags
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
