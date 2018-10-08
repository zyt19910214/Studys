# -*- coding: utf-8 -*-

from scrapy import cmdline
import sys
# sys.argv =['<path>/scrapy.py', 'crawl', 'xxx']
cmdline.execute("scrapy crawl lj".split())
