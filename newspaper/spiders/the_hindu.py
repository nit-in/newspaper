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


class TheHinduSpider(scrapy.Spider):
    name = "the_hindu"
    allowed_domains = [config.THE_HINDU_ROOT]
    tag = ""
    namespaces = ["th", "http://schemas.datacontract.org/2004/07/SphereUp.Data"]

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
                    yield scrapy.Request(url, self.parse_node)

    def parse_node(self, response):
        response.selector.register_namespace(self.namespaces[0], self.namespaces[1])
        date = response.xpath("//th:Date//text()").get()
        date = date[:10]
        date = datetime.strptime(date, "%Y-%m-%d").strftime("%d-%b-%Y")
        the_hindu_link = response.xpath("//th:Url//text()").get()
        article_name = response.xpath("//th:Name//text()").get()
        self.tag = self.tag.replace("%20", "_")
        self.tag = self.tag.strip()
        self.tag = self.tag.title()

        mpdf = make_pdf(
            str(self.name),
            str(the_hindu_link),
            str(date),
            str(self.tag),
            str(article_name),
        )
        mpdf.print()
