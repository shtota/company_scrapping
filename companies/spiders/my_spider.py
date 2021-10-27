import scrapy
import pandas as pd
from bs4 import BeautifulSoup
import re


class CompanySpider(scrapy.Spider):
    name = "company"
    start_urls = ['https://{}/'.format(website) for website in pd.read_csv('to_parse.csv').website.values[:5000]]

    def parse(self, response):
        print(response.url)
        soup = BeautifulSoup(response.body, 'html.parser')
        clean_text = re.sub(' +', ' ', soup.get_text().replace('\n', ' ')).strip().split(' ')
        if len(clean_text) > 50:
            yield {'url': response.url, 'text': clean_text}