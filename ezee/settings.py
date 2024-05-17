# Scrapy settings for ezee project

BOT_NAME = "ezee"

SPIDER_MODULES = ["ezee.spiders"]
NEWSPIDER_MODULE = "ezee.spiders"


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

USER_AGENT = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36'


LOG_ENABLED = True
LOG_LEVEL = 'INFO'

# download settings
DOWNLOAD_DELAY = .25
DOWNLOAD_TIMEOUT = 5
RANDOMIZE_DOWNLOAD_DELAY = True
AUTOTHROTTLE_ENABLED = True
CONCURRENT_ITEMS = 50

AUTOTHROTTLE_TARGET_CONCURRENCY = 5

#other settings
COOKIES_ENABLED = True
RETRY_ENABLED = True
REDIRECT_ENABLED = True
AJAXCRAWL_ENABLED = False
REACTOR_THREADPOOL_MAXSIZE = 5
DNS_RESOLVER = "scrapy.resolver.CachingHostnameResolver"
HTTPCACHE_ENABLED = False
RETRY_HTTP_CODES = [429]
RETRY_TIMES = 3


ITEM_PIPELINES = {
    'ezee.pipelines.EzeePipeline': 1,
    'scrapy.pipelines.images.ImagesPipeline': 2,
}

#
#IMAGES_STORE = "images/"
IMAGES_STORE = "s3://proco-take-home-assignment-aakash/aakash_mahawar/"
IMAGES_STORE_S3_ACL = "public-read"



AWS_ACCESS_KEY_ID = 'xxxx'
AWS_SECRET_ACCESS_KEY = 'xxxx'
AWS_DEFAULT_ACL = None
