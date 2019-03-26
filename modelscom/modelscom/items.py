# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ModelscomItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    image_urls = scrapy.Field()
    # 杂志名
    magazine = scrapy.Field()
    # 发布日期
    published = scrapy.Field()
    # 摄影师
    photographer = scrapy.Field()
    pass
