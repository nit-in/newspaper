#!/usr/bin/python3
import scrapy
from yarl import URL
import subprocess
import os.path
from datetime import datetime
import functools
from progress.bar import Bar
import json
import newspaper.spiders.config as config
from newspaper.spiders.generate_links import generate_links as generate
from newspaper.spiders.makepdf import make_pdf


class BusinessStandardSpider(scrapy.Spider):

    name = "business_standard"
    allowed_domains = [config.BUSINESS_STANDARD_ROOT]
    tag = ""

    def start_requests(self):
        with open(config.JSON_FILE) as json_file:
            terms = json.load(json_file)
            lower_range = int(terms["lower_value"])
            upper_range = int(terms["upper_value"])
            terms = terms["search"]
            for term in terms:
                self.tag = term
                urls = generate(self.name, term)
                for url in urls:
                    yield scrapy.Request(url, self.parse)

    def parse(self, response):
        response_links = response.css("a::attr(href)").getall()
        for response_link in response_links:
            response_link = str(response_link[3:-2])
            response_link = str(config.BUSINESS_STANDARD_ROOT) + response_link.replace(
                "\\", ""
            )
            url = URL(response_link)
            try:
                # get date
                article = url.parts[3]
                date = str(20) + str(article[-18:-12])
                date = datetime.strptime(date, "%Y%m%d").strftime(
                    "%d-%b-%Y"
                )  # in format dd-mmm-yyyy
                # get article no for printing page as business-standard has a print page
                business_standard_link = config.BUSINESS_STANDARD_PRINT + str(
                    article[-19:-5]
                )
                article_name = article[:-20]
                self.tag = self.tag.replace("%20", "_")
                self.tag = self.tag.strip()
                self.tag = self.tag.title()
                mpdf = make_pdf(
                    str(self.name),
                    str(business_standard_link),
                    str(date),
                    str(self.tag),
                    str(article_name),
                )
                mpdf.print()

            except IndexError:
                pass
