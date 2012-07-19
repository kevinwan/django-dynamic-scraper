from scrapy.item import Item, Field

class Product(Item):
    title = Field()    
    url = Field()
    price = Field()
    time = Field()
    #meta = Field()
    #last_updated = Field(serializer=str)
  
    def __str__(self):
        return "product: %s" % (self.get('title'))
