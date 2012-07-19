from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import BaseSgmlLinkExtractor
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor,
from scrapy.selector import HtmlXPathSelector
from dirbot.items import Website


class DmozSpider(CrawlSpider):
    name = "dmoz_1"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/"
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
        sites = hxs.select('//ul[@class="directory-url"]/li')
        
        items=[]   
        for site in sites:
            item = Website()
            item['name'] = site.select('a/text()').extract()
            item['url'] = site.select('a/@href').extract()
            item['description'] = site.select('text()').extract()
            items.append(item)
        return items
    
    
    
    
    
    
    
