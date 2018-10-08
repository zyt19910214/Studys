# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class VipscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 标题
    url = scrapy.Field()  # 链接
    image_url = scrapy.Field() #图片链接

class ImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
