# -*- coding: utf-8 -*-

"""
@version: python2.7
@author: 'zyt'
@software: PyCharm
@time: 2018/5/3 20:05
"""
import scrapy


class taoPiaoSpider(scrapy.Spider):
    # 爬虫名称
    name = "taopiao"
    start_urls = [
        "https://www.taopiaopiao.com/showList.htm?n_s=new"
    ]

    def parse(self, response):
        # 实现网页的解析
        movics = response.xpath("//div[@class='movie-card-wrap']")
        for movic in movics:
            url = movic.xpath("a/@href").extract()[0]
            name = movic.xpath("a/div[@class='movie-card-name']/span[@class='bt-l']/text()").extract()[0]
            f = open('1.txt','a')
            f.write(name.encode('utf-8')+'\n')
            f.close()
