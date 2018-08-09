# -*- coding: utf-8 -*-
import scrapy
import pymongo


class MiaHTMLSpider(scrapy.Spider):
    name = 'mia_html'
    allowed_domains = ['miabellebaby.com']

    def start_requests(self):
        '''Get urls from mongodb'''
        mongo_db = self.settings.get('MONGO_DATABASE')
        # TODO changot URI to host & port
        mongo_uri = self.settings.get('MONGO_URI')
        client = pymongo.MongoClient(mongo_uri)
        db = client[mongo_db]

        for product in db['Product'].find():
            url = product.get('url')
            if url:
                yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for quote in response.css('item'):
            print(quote.xpath('//meta/@content').extract_first())
            yield {
                'title': quote.xpath('//meta[contains(@property, "title")]/@content').extract_first()
            }
