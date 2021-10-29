import scrapy
import pandas as pd
from bs4 import BeautifulSoup
import re


class CompanySpider(scrapy.Spider):
    name = "company"

    def __init__(self, chunk=0, *args, **kwargs):
        super(CompanySpider, self).__init__(*args, **kwargs)
        self.start_urls = pd.read_csv('./targets/{}.csv'.format(chunk)).website.values

    def start_requests(self):
        for index, url in enumerate(self.start_urls):
            yield scrapy.Request('https://{}/'.format(url), callback=self.parse,
                                 cb_kwargs={'index':index, 'original_url': url})

    def parse(self, response, index, original_url):
        self.logger.critical('Parsing index: {}'.format(index))
        soup = BeautifulSoup(response.body, 'html.parser')
        clean_text = re.sub(' +', ' ', soup.get_text().replace('\n', ' ')).strip().split(' ')
        if len(clean_text) > 50:
            yield {'index':index, 'original_url': original_url,'url': response.url, 'text': clean_text}