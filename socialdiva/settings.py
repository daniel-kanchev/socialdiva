BOT_NAME = 'socialdiva'
SPIDER_MODULES = ['socialdiva.spiders']
NEWSPIDER_MODULE = 'socialdiva.spiders'
ROBOTSTXT_OBEY = True
LOG_LEVEL = 'WARNING'
ITEM_PIPELINES = {
   'socialdiva.pipelines.DatabasePipeline': 300,
}

COOKIES_ENABLED = False
DOWNLOAD_DELAY = 3
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36" \
             " (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36"
