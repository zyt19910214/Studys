# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
import json
import codecs
class VipscrapyPipeline(object):

    def __init__(self):
        self.file = codecs.open('info.json', 'w', encoding='utf-8')  # 保存为json文件

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"  # 转为json的
        self.file.write(line)  # 写入文件中
        return item



class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url)

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem('Item contains no images')
        item['image_paths'] = image_path
        return item