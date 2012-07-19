# Scrapy settings for dirbot project

BOT_NAME = 'dirbot'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['dirbot.spiders']
NEWSPIDER_MODULE = 'dirbot.spiders'
DEFAULT_ITEM_CLASS = 'dirbot.items.Product'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = ['dirbot.pipelines.FilterWordsPipeline']

#DEFAULT_RESPONSE_ENCODING = 'utf-8'

#DEFAULT_REQUEST_HEADERS = {
#    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }