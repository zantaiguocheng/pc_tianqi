# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule

from tianqi.items import TianqiItem


class LstqSpider(CrawlSpider):
    name = 'lstq'
    allowed_domains = ['www.tianqihoubao.com']
    start_urls = ['http://www.tianqihoubao.com/lishi/chengdu.html']

    rules = (
        Rule(LinkExtractor(allow=r'month/\d+\.html'),
             callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = TianqiItem()
        x = Selector(response)
        rq_list = x.re('(\d+年\d+月\d+日)')
        tqzk_list = x.re('([\u4e00-\u9fa5]+\s+/[\u4e00-\u9fa5]+)')[::2]
        qw_list = x.re('\d+℃\s+/\s+-?\d+℃')
        for i in range(len(tqzk_list)):
            item['rq'] = rq_list[i]
            item['tqzk'] = re.sub('\s+', '', tqzk_list[i])
            item['qw'] = re.sub('\s+', '', qw_list[i])
            yield item
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
x.re('作者</span.*?</a></span></span>')