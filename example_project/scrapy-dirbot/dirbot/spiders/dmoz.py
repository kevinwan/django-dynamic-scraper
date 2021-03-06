from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
#from scrapy.http import Request

from dirbot.items import Product


class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["shanghai.baixing.com"]
    start_urls = [
        "http://shanghai.baixing.com/ershouqiche/m11437/",
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        #url_dir = hxs.select('//ul[@class="directory"]/li/a/@href')
        lists = hxs.select('//ul[@id="listingHead"]/li')
        
        items = []     
  
        for car in lists:
            item = Product()
            item['title'] = car.select('div[@class="list-item-content"]//a/text()').extract()[0]
            item['url'] =  car.select('div[@class="list-item-content"]//a/@href').extract()[0]          
            #item['meta'] = car.select('div//div/text()').extract()[1]
            #item['meta'] = car.select('div//div[@class="list-item-content-meta"]/text()').extract()
            item['time'] =  car.select('span[@class="list-item-block"]/time//text()').extract()[0]
            item['price'] = car.select('span[@class="list-item-block"]/cite/text()').extract()[0]
            print item['time']+":::"+item['price']+":::"+item['title']
            items.append(item)
        return items
    
