# -*- coding: utf-8 -*-
import scrapy
from hellospider.items import HellospiderItem

class MyspiderSpider(scrapy.Spider):
    """
    name:scrapy唯一定位实例的属性，必须唯一
    allowed_domains：允许爬取的域名列表，不设置表示允许爬取所有
    start_urls：起始爬取列表
    """

    name = 'Myspider'
    allowed_domains = ['baidu.com']
    # 设置爬取地址列表
    box = []
    for num in range(301):
        if num % 50 == 0:
            pages = 'http://tieba.baidu.com/f?kw=%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB&ie=utf-8&&pn={0}'.format(num)
            print("page:" + pages)
            box.append(pages)
        else:
            continue
    # 填写爬取地址
    start_urls = box
    # print(box) 用于测试






    #start_urls = ['http://baidu.com/']

    def parse(self, response):
        for line in response.xpath('//li[@class=" j_thread_list clearfix"]'):
            # 初始化item对象保存爬取的信息
            item = HellospiderItem()
            # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
            #  item['id'] = line.xpath(
            #      './/div[contains(@class,"threadlist_title pull_left j_th_tit ")]/a/@href').extract()[0][3:6]
            item['title'] = line.xpath(
                './/div[contains(@class,"threadlist_title pull_left j_th_tit ")]/a/text()').extract()[0]
            item['author'] = line.xpath(
                './/div[contains(@class,"threadlist_author pull_right")]//span[contains(@class,"frs-author-name-wrap")]/a/text()').extract()[
                0]
            item['reply'] = line.xpath(
                './/div[contains(@class,"col2_left j_threadlist_li_left")]/span/text()').extract()[0]
            yield item

