#!/usr/bin/python3
import scrapy
from yarl import URL
from datetime import datetime
import json
import newspaper.spiders.config as config
from newspaper.spiders.generate_links import generate_links as generate
from newspaper.spiders.makepdf import make_pdf


class IndianExpressSpider(scrapy.Spider):
    name = "indian_express"
    allowed_domains = [config.INDIAN_EXPRESS_ROOT]
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
        response_links = response.css("div.details")
        for response_link in response_links:
            anchor = response_link.css("h3 a::attr(href)").get()
            name = response_link.css("h3 a::text").get()
            article_name = name.replace(" ", "_")
            indian_express_link = str(anchor)
            try:
                date_list = response_link.css("time::text").getall()
                date_list.reverse()
                date = str(date_list[0])
                date = date[14:-11].replace(" ", "")
                date = datetime.strptime(date, "%B%d,%Y").strftime("%Y-%b-%d")
                print(date)
                mpdf = make_pdf(
                    str(self.name),
                    str(indian_express_link),
                    str(date),
                    str(self.tag),
                    str(article_name),
                )
                mpdf.print()
            except IndexError:
                pass
