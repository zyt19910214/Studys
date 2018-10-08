# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LjItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()  # 小区名称
    type = scrapy.Field()  # 房屋类型
    status = scrapy.Field() #房屋状态
    location = scrapy.Field() # 小区位置
    area = scrapy.Field() # 建筑面积
    price = scrapy.Field() # 房屋价格
    tag = scrapy.Field() # 标签