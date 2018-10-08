#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc :
"""
from vipscrapy.items import VipscrapyItem
from vipscrapy.items import ImageItem
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup

import re
class VipSpider(scrapy.spiders.Spider):
    name = "vip"
    allowed_domains = ["iqiyi.com"]
    image_url = []
    start_urls = [
        "http://www.iqiyi.com/dianying_new/i_list_paihangbang.html"
    ]

    def parse(self, response):
        soup = BeautifulSoup(response.body,'lxml')
        item = VipscrapyItem()
        item_image = ImageItem()
        # item['name'] = soup.find('h1').text
        # item['posttime'] = soup.find('a',class_='site-piclist_pic_link').text
        p_list = soup.find_all('div',class_='site-piclist_pic')
        port_1 = 'http://www.wmxz.wang/video.php?url='
        for p in  p_list:
            name = p.find('a').get('title')
            link = p.find('a').get('href')
            image = p.find('img').get('src')
            item['name'] = name
            item['url'] = port_1+link
            item['image_url'] = image
            self.image_url.append(image)
            yield item
        item_image['image_urls'] = self.image_url
        yield item_image


