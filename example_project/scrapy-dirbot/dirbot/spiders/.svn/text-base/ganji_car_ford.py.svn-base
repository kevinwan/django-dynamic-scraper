from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import BaseSgmlLinkExtractor
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor,
from scrapy.selector import HtmlXPathSelector
from dirbot.items import Product


class DmozSpider(CrawlSpider):
    name = "ganji_car_ford"
    allowed_domains = ["sh.ganji.com"]
    start_urls = [
        "http://sh.ganji.com/ford/a2/"
    ]

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        #Rule(SgmlLinkExtractor(allow=('Books', ), deny=('Ruby', )), callback='parse_item'),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        #Rule(SgmlLinkExtractor(allow=('Resources','Books','Articles_and_Reviews', 'Personal_Pages' )), callback='parse_item'),
        #Rule(SgmlLinkExtractor(allow=('Resources','Books','Articles_and_Reviews', 'Personal_Pages' )), callback='parse_item'),
        Rule(BaseSgmlLinkExtractor(),callback='parse_item'),
    )

    def parse_item(self, response):
        
        self.log('Page : %s' % response.url)
        hxs = HtmlXPathSelector(response)
#        url_dir = hxs.select('//ul[@class="directory"]/li/a/@href').extract()
        #lists = hxs.select('//div[@class="list"]/dl[@class="list-car"]')
        lists = hxs.select('//div[@class="list"]/dl[@class="list-car"]')
        
        items=[]   
        for car in lists:
            item = Product()
            item['title'] = car.select('dt/a/@title').extract()
            item['url'] = car.select('dt/a/@href').extract()
            #item['description'] = car.select('text()').extract()
            #item['time'] = car.select('dd[@class="time"]/text()').extract()
            #item['price'] = car.select('dd[@class="price"]/text()').extract()
       
            items.append(item)
        return items
    
    
    
    
    
    
    
