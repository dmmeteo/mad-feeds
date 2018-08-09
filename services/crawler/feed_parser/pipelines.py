# -*- coding: utf-8 -*-
import pymongo
from scrapy.exceptions import DropItem


class MongoPipeline(object):

    collection_name = 'Product'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # TODO insert items locale data in locale-fields (en, il, ru)
        if spider.name == 'mia_feed':
            if item['price']:
                link = item['link'].split('?')[0]
                item['link'] = link
                self.db[self.collection_name].update({'product_id': item['product_id']}, dict(item), upsert=True)
            else:
                raise DropItem("Missing price in %s" % item)
        else:
            raise DropItem('Not mia_feed spider')

