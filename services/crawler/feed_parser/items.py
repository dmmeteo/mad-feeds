# -*- coding: utf-8 -*-
import scrapy

class ProductFeedItem(scrapy.Item):
    '''
    Defining the storage containers for the data we
    plan to scrape
    '''
    product_id = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()
    image_link = scrapy.Field()
    color = scrapy.Field()
    size = scrapy.Field()
    pattern = scrapy.Field()
    material = scrapy.Field()
    gender = scrapy.Field()

    # #Shopify fields
    product_type = scrapy.Field()
    brand = scrapy.Field()
    gtin = scrapy.Field()
    mpn = scrapy.Field()
    price = scrapy.Field()
    compare_at_price = scrapy.Field()
    sale_price = scrapy.Field()
    tags = scrapy.Field()

    # #Facebook fields
    labels = scrapy.Field()
    availability = scrapy.Field()
    condition = scrapy.Field()
    item_group_id = scrapy.Field()
    shipping_weight = scrapy.Field()

    # #Google fields
    google_product_category = scrapy.Field()
    custom_label_0 = scrapy.Field()
    custom_label_1 = scrapy.Field()
    custom_label_2 = scrapy.Field()
    custom_label_3 = scrapy.Field()
    custom_label_4 = scrapy.Field()
    age_group = scrapy.Field()

