#!/usr/bin/python3
import scrapy
from yarl import URL
import subprocess
import os.path
from datetime import datetime
import functools
from progress.bar import Bar
import json
import re
import newspaper.spiders.config as config
from newspaper.spiders.generate_links import generate_links as generate
from newspaper.spiders.makepdf import make_pdf


class LivemintSpider(scrapy.Spider):
    name = 'livemint'
    allowed_domains = [config.LIVEMINT_ROOT]
    tag = ""

    def start_requests(self):
        with open(config.JSON_FILE) as json_file:
                terms = json.load(json_file)
                lower_range = int(terms["lower_value"])
                upper_range = int(terms["upper_value"])
                terms = terms["search"]
                for term in terms:
                    self.tag = term
                    urls = generate(self.name,term)
                    for url in urls:
                        yield scrapy.Request(url, self.parse)
    
    def parse(self, response):
        response_links = response.css(".headlineSec")
        for response_link in response_links:
            anchor = response_link.css("a::attr(href)").get()
            date = response_link.css("span::attr(data-updatedlongtime)").get()
            article_name = anchor
            date = date.replace(" ", "")
            date = date[:10]
            #            fdname = fdname.replace(",","") not needed
            try:
                date= datetime.strptime(date, "%d%b%Y").strftime("%d-%b-%Y")
            except ValueError:
                today = datetime.today()
                date = datetime.strftime(today, "%d-%b-%Y")
                
            try:
                    anchor = re.search("-(\d+).html", anchor).group(1)
            except AttributeError:
                    print("attrib error" + str(anchor))
            livemint_link = str(config.LIVEMINT_PRINT) + str(anchor)
            article_name = article_name[:-20]
            self.tag = self.tag.replace("%20","_")
            self.tag = self.tag.strip()
            self.tag = self.tag.title()
            mpdf = make_pdf(str(self.name),str(livemint_link),str(date),str(self.tag),str(article_name))
            mpdf.print()
