# -*- coding: utf-8 -*-
import scrapy

class ProductItem(scrapy.Item):
    '''
    Defining the storage containers for the data we
    plan to scrape
    '''
    product_id = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    # color
    # size
    # pattern
    # material
    # gender

    # # Other Shopify fields
    # product_type
    # brand
    # gtin
    # mpn
    # price
    # google_product_category

    # compare_at_price
    # sale_price
    # tags

    # #Facebook fields
    # labels
    # availability
    # condition
    # item_group_id
    # shipping_weight

    # #Google fields
    # google_product_category
    # custom labels
    # age group
    # condition
    # gender

