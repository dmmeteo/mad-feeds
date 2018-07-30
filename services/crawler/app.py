# -*- coding: utf-8 -*-
import scrapy
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from feed_parser.spiders import MiaFeedSpider, MiaHTMLSpider


configure_logging()
runner = CrawlerRunner()

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(MiaFeedSpider)
    yield runner.crawl(MiaHTMLSpider)
    reactor.stop()


if __name__ == '__main__':
    crawl()
    reactor.run()
