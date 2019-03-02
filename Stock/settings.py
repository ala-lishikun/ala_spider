# -*- coding: utf-8 -*-

# Scrapy settings for Stock project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'notice'

SPIDER_MODULES = ['Stock.spiders']
NEWSPIDER_MODULE = 'Stock.spiders'
ITEM_PIPELINES = {'Stock.pipelines.StockPipeline':1}

COOKIES_ENABLED = False
COOKIES_ENABLES = False
DEPTH_LIMIT = 100


