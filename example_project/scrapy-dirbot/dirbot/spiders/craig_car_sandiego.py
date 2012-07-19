from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import BaseSgmlLinkExtractor
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor,
from scrapy.selector import HtmlXPathSelector
from dirbot.items import Product


class DmozSpider(CrawlSpider):
    name = "craig_car_sandiego"
    allowed_domains = ["sandiego.craigslist.org"]
    start_urls = [
        "http://sandiego.craigslist.org/cto/",
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
        lists = hxs.select('//p[@class="row"]')
        
        items=[]   
        for car in lists:
            item = Product()
            item['title'] = car.select('a/text()').extract()
            item['url'] = car.select('a/@href').extract()
            item['price'] = car.select('a/span[@class="itempp"]/text()').extract()
            #item['time'] = car.select('dd[@class="time"]/text()').extract()
            #item['price'] = car.select('dd[@class="price"]/text()').extract()
       
            items.append(item)
        return items
    
    
    
    
    
    
    
