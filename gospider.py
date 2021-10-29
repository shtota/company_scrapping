from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from companies.spiders.my_spider import CompanySpider
from sys import argv

if len(argv) > 1:
    chunk = int(argv[-1])
else:
    print('Provide start chunk as arguments')
    print(len(argv), argv)
    raise NotImplementedError

try:
    settings = get_project_settings()
    settings.set('FEED_FORMAT', 'json')
    settings.set('FEED_URI', '{}.json'.format(chunk))
    process = CrawlerProcess(settings)
    process.crawl(CompanySpider, chunk=chunk, loglevel='INFO')
    process.start()

    with open('success{}'.format(chunk), 'w') as f:
        f.write(' ')
except KeyboardInterrupt:
    print('exiting')
except:
    with open('success{}FAIL'.format(chunk), 'w') as f:
        f.write(' ')
