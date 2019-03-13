# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib.request
import os

class ModelscomPipeline(object):
    def process_item(self, item, spider):
        file_name = item['name']
        file_path = os.path.join("D:\\workspace\\models.com_spider\\pic", file_name)
        urllib.request.urlretrieve(item['mp4_url'], file_path)
        return item
