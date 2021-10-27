from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from companies.spiders.my_spider import CompanySpider
from sys import argv

chunk = '14'
if len(argv) > 1:
    chunk = argv[-1]


settings = get_project_settings()
settings.set('FEED_FORMAT', 'json')
settings.set('FEED_URI', '{}.json'.format(chunk))
process = CrawlerProcess(settings)
process.crawl(CompanySpider, chunk=int(chunk), loglevel='INFO')
process.start()