# -*- coding: utf-8 -*-
from Stock import settings
from scrapy import cmdline

cmdline.execute("scrapy crawl notice -o info.csv".split())