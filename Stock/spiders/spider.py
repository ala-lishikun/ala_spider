# -*- coding: utf-8 -*-
import scrapy
import sys
import time
reload(sys)
sys.setdefaultencoding("utf-8")
from scrapy.spiders import CrawlSpider
from Stock.items import StockItem
from scrapy import Request
from scrapy.selector import Selector
from scrapy.selector import HtmlXPathSelector




class Stock_notice(CrawlSpider):
    name = "notice"
    download_delay = 1
    allowed_domains = ["data.10jqka.com.cn"]
    start_urls = ["http://data.10jqka.com.cn/market/ggsd/board/2/order/asc/page/1/ajax/1/"]



    def parse(self, response):

        notices = response.xpath('//table/tbody/tr')
        for notice in notices:
            item = StockItem()
            item['notice_time'] = notice.xpath('td[2]/text()').extract()
            item['stock_code'] = notice.xpath('td[3]/a/text()').extract()
            item['stock_name'] = notice.xpath('td[4]/a/text()').extract()
            item['notice_title'] = notice.xpath('td[7]//a/text()').extract()
            item['notice_href'] = notice.xpath('td[7]//a/@href').extract()
            yield item

        # next_page = response.xpath('//div[@class="m-page J-ajax-page"]/a[8]/@href').extract()
        #
        # if next_page:
        #     request_url = response.urljoin(next_page)
        #     print (request_url)
        #     yield Request(request_url, callback=self.parse)
        for i in range(1, 20):
            next_page = "http://data.10jqka.com.cn/market/ggsd/board/2/order/asc/page/"+str(i)+"/ajax/1/"
            yield Request(next_page, callback=self.parse)