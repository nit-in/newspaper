#!/usr/bin/python3
import scrapy
from datetime import datetime
import json
import re
import newspaper.spiders.config as config
from newspaper.spiders.generate_links import generate_links as generate
from newspaper.spiders.makepdf import make_pdf


class LivemintSpider(scrapy.Spider):
    name = "financial_express"
    allowed_domains = [config.FINANCIAL_EXPRESS_ROOT]
    tag = ""

    def start_requests(self):
        with open(config.JSON_FILE) as json_file:
            terms = json.load(json_file)
            terms = terms["search"]
            for term in terms:
                self.tag = term
                urls = generate(self.name, term)
                for url in urls:
                    yield scrapy.Request(url, self.parse)

    def parse(self, response):
        response_links = response.css(".content-list")
        for response_link in response_links:
            anchor = response_link.css("h3 a::attr(href)").get()
            date = response_link.css(".minsago::text").get()
            date = date.replace(" ","")
            title = response_link.css("h3 a::text").get()
            try:
                date = datetime.strptime(date,"%b%d,%Y").strftime("%Y-%b-%d")
            except ValueError:
                today = datetime.today()
                date = datetime.strftime(today, "%Y-%b-%d")
            self.tag = self.tag.replace("%20", "_")
            self.tag = self.tag.strip()
            self.tag = self.tag.title()
            financial_express_link = str(anchor)
            article_name = str(re.sub('\W+','_', title))
            mpdf = make_pdf(
                str(self.name),
                str(financial_express_link),
                str(date),
                str(self.tag),
                str(article_name),
            )
            mpdf.print()

