# -*- coding: utf-8 -*-
import scrapy
import os
from modelscom.items import ModelscomItem
class ModelsSpider(scrapy.Spider):
    name = 'models'
    # 允许访问的域
    allowed_domains = ['models.com']
    # 初始URL
    start_urls = ['http://models.com/']

    def parse(self, response):
        item = ModelscomItem()
        item['image_urls'] = response.xpath('//img//@src').extract()
        print 'image_urls',item['image_urls']
        yield item

