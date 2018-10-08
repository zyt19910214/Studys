#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc :
"""
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
from Mzt.items import MztItem
from scrapy import Request
import os

class MztSpider(scrapy.spiders.Spider):
    name = "Mzt"
    allowed_domains = ["m.mzitu.com"]
    link_urls = []
    image_url = []
    start_urls = [
        "http://m.mzitu.com/page/1"
    ]


    def parse(self, response):
        item = MztItem()
        soup = BeautifulSoup(response.body,'lxml')
        url_list = soup.find_all('a')
        for url in url_list:
            x = url.find_all('img', class_='featured-image aligncenter lazy')
            if x:
                s_url = url.get('href')
                item['url'] = s_url
                self.link_urls.append(s_url)
                yield Request(s_url,callback=self.paser2)

    def paser2(self,response):
        print ('11111111')
        item = MztItem()
        yield item
