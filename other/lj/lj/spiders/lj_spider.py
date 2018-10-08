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
from lj.items import LjItem

class VipSpider(scrapy.spiders.Spider):
    name = "lj"
    allowed_domains = ["xa.fang.lianjia.com"]
    image_url = []
    start_urls = [
        "https://xa.fang.lianjia.com/loupan/"
    ]

    def parse(self, response):

        item = LjItem()
        soup = BeautifulSoup(response.body,'lxml')

        y=soup.find("div",attrs={"class":"resblock-have-find"}).find('span',attrs={"class":"value"}).text
        lp = soup.find_all("div", attrs={"class": "resblock-desc-wrapper"})

        for l in lp:
            resblock_name = l.find("div", attrs={"class": "resblock-name"})
            name = resblock_name.find('a',attrs={'class','name'}).text
            item['name'] = name
            print(u'小区名称：'+name)

            type = resblock_name.find('span',attrs={'class','resblock-type'}).text
            item['type'] = type
            print(u'房屋类型：' +type)

            status = resblock_name.find('span',attrs={'class','sale-status'}).text
            item['status'] = status
            print(u'房屋状态：' +status)

            location = l.find("div", attrs={"class": "resblock-location"})
            location_list = location.text.split('\n/')
            item['location'] = location_list[0].strip()+'-'+location_list[1].strip()+'-'+location_list[2].strip()
            print (u'小区位置：'+location_list[0].strip()+'-'+location_list[1].strip()+'-'+location_list[2].strip())

            area = l.find("div", attrs={"class": "resblock-area"})
            item['area'] = area.text.strip()
            if area.text=='':
                print(u'建筑面积：无')
            else:
                print(u'建筑面积：'+area.text.strip())

            price = l.find("div", attrs={"class": "resblock-price"})
            item['price'] = price.text.replace('\n','')
            print (u'房屋价格：'+price.text.replace('\n',''))

            tag = l.find("div", attrs={"class": "resblock-tag"})
            item['tag'] = tag.text.strip().replace('\n','|')
            print (u'标签：'+tag.text.strip().replace('\n','|'))

            yield item

        for x in range(2,int(y)/10+1):
            yield scrapy.Request('https://xa.fang.lianjia.com/loupan/pg'+str(x), callback=self.parse)


