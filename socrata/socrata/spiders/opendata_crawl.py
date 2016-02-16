# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from socrata.items import SocrataItem


class OpendataSpider(CrawlSpider):
    name = "opendata_crawl"
    allowed_domains = ["opendata.socrata.com"]
    start_urls = (
        'https://opendata.socrata.com/',
    )
    rules = [
        Rule(LinkExtractor(allow='browse\?utf8=%E2%9C%93&page=\d*'),
             callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        titles= response.xpath('//tr[@itemscope="itemscope"]')
        for title in titles:
            item=SocrataItem()
            item["text"]=title.select("td[2]/a/span/text()").extract()
            item["url"]=title.select("td[2]/a/@href").extract()
            item["views"]=title.select("td[3]/span/text()").extract()
            yield item

