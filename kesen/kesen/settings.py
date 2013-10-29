# Scrapy settings for kesen project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'kesen'

SPIDER_MODULES = ['kesen.spiders']
NEWSPIDER_MODULE = 'kesen.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'kesen (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
        'kesen.pipelines.KesenPipeline': 100
        }
