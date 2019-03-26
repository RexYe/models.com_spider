# -*- coding: utf-8 -*-
import scrapy
import os
from modelscom.items import ModelscomItem
from scrapy import FormRequest,Request

class ModelsSpider(scrapy.Spider):
    name = 'models'
    # 允许访问的域
    allowed_domains = ['models.com']
    # 初始URL
    start_urls = ['https://models.com/db/editorial/']
    # 登录url
    login_url = 'https://models.com/account/'

    def parse(self, response):
        # print(response.text)
        image = response.xpath('//img//@src').extract()
        print("image:::", image)
        # for i in image:
        #     item = ModelscomItem()
        #     item['image_urls'] = i[21:-1]
        #     print 'image_urls:',item['image_urls']
        # yield item

    def start_requests(self):
        yield scrapy.Request(self.login_url,callback=self.login)

    def login(self,response):
        formdata = {
             'USERID':'894450343@qq.com','PASSWORD':'123456'}
        yield FormRequest.from_response(response,formdata=formdata,
                                         callback=self.parse_login)
    def parse_login(self,response):
        # print('>>>>>>>>'+response.text)
        if 'Welcome' in response.text:
            print('login success')
            yield scrapy.Request(self.start_urls[0], callback=self.parse)