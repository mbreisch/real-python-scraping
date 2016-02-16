# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector
from wikipedia.items import WikipediaItem
from urlparse import urljoin


class WikiSpider(Spider):
    name = "wiki"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = (
        'https://en.wikipedia.org/wiki/Category:2014_films',
    )

    def parse(self, response):
        titles=Selector(response).xpath('//div[@id="mw-pages"]//li')

        for title in titles:
            item=WikipediaItem()
            url=title.select("a/@href").extract()
            if url:
                item["title"]=title.select("a/text()").extract()
                item["url"]=urljoin("http://en.wikipedia.org",url[0])
                yield item
