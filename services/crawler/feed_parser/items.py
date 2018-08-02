# -*- coding: utf-8 -*-
import scrapy

class Product(scrapy.Item):
    '''
    Defining the storage containers for the data we
    plan to scrape
    '''
    pk = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()

