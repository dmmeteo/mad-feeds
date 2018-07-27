# -*- coding: utf-8 -*-
import scrapy

class RedditItem(scrapy.Item):
    '''
    Defining the storage containers for the data we
    plan to scrape
    '''
    date = scrapy.Field()
    date_str = scrapy.Field()
    sub = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    score = scrapy.Field()
    commentsUrl = scrapy.Field()
