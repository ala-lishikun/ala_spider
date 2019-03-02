# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


from scrapy import Item, Field
class StockItem(Item):
    stock_code = Field()
    stock_name = Field()
    notice_title = Field()
    notice_href = Field()
    notice_time = Field()

