# -*- coding: utf-8 -*-
from datetime import date
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from feed_parser.spiders import MiaFeedSpider, MiaHTMLSpider

if __name__ == '__main__':
    # only run on saturdays (once a week)
    # if date.strftime(date.today(), '%A').lower() == 'saturday':
    process = CrawlerProcess(get_project_settings())

    # at first run MiaFeed
    process.crawl(MiaFeedSpider)
    process.start()

    # at second run MiaHTML
    process.crawl(MiaHTMLSpider)
    process.start() # the script will block here until the crawling is finished
