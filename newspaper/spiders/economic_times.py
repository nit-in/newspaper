#!/usr/bin/python3
import scrapy
from datetime import datetime
import json
import newspaper.spiders.config as config
from newspaper.spiders.generate_links import generate_links as generate
from newspaper.spiders.makepdf import make_pdf


class EconomicTimesSpider(scrapy.Spider):
    name = "economic_times"
    allowed_domains = [config.ECONOMIC_TIMES_ROOT]
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
        response_links = response.css("div")
        for response_link in response_links:
            anchor = response_link.css("a::attr(href)").get()
            date = response_link.css("time::text").get()
            date = date.replace(" ", "")
            date = date[:10]
            #            fdname = fdname.replace(",","") not needed
            date = datetime.strptime(date, "%d%b,%Y").strftime("%Y-%b-%d")
            anchor = anchor.replace("articleshow", "printarticle")
            economic_times_link = str(config.ECONOMIC_TIMES_ROOT) + str(anchor)
            article_name = anchor[:-26]
            self.tag = self.tag.replace("%20", "_")
            self.tag = self.tag.strip()
            self.tag = self.tag.title()
            article_name_list = str(article_name).split("/")
            article_name_list.reverse()
            try:
                article_name = article_name_list[0]
                article_name = article_name.replace(" ","_")
                mpdf = make_pdf(
                    str(self.name),
                    str(economic_times_link),
                    str(date),
                    str(self.tag),
                    str(article_name),
                )
                mpdf.print()
            except IndexError:
                print(f"Index error: {article_name}")
