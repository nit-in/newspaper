#!/usr/bin/python3
import newspaper.spiders.config as config
import pdfkit
from pathlib import Path
from itertools import chain
import time
from stringcolor import *
from datetime import datetime

# fields = ["Newspaper", "File_Name", "Link"]


class make_pdf:
    """generate pdf from newspaper links,also csv files for successful and failed downloads"""

    def __init__(self, newspaper, link, article_date, tag, file_name):
        self.newspaper = newspaper
        self.link = link
        self.article_date = article_date.replace("-", "/")
        self.tag = tag
        self.file_name = file_name
        self.folder = (
            str(config.ROOT_DIR)
            + str(self.newspaper)
            + "/"
            + str(self.article_date)
            + "/"
            + str(self.tag)
            + "/"
        )
        self.pdf = self.folder + self.file_name + ".pdf"
        self.pdf_path = Path(self.pdf)
        self.pdf_path = self.pdf_path.expanduser()

    def print(self):
        print(cs("Working...", "blue4"))
        options = config.PDFKIT_OPTIONS
        if self.pdf_path.parent.is_dir():
            string = f"\nFolder: {self.pdf_path.parent} already exists"
            print(cs(string, "orchid"))
        else:
            string = f"\nmaking {self.pdf_path.parent} folder"
            print(cs(string, "olive"))
            self.pdf_path.parent.mkdir(parents=True)
        # self.file_name = os.path.join(self.folder,self.file_name + ".pdf")
        if self.check_date(self.article_date):

            if (
                self.pdf_file_exists(self.pdf_path.name)
                and int(self.pdf_path.lstat().st_size) > 25600
            ):
                string2 = f"\nFile: {self.pdf_path} already downloaded"
                print(cs(string2, "magenta"))
            else:
                string2 = f"\nDownloading: {self.pdf_path}"
                print(cs(string2, "springgreen2"))
                pdfkit.from_url(str(self.link), str(self.pdf_path), options=options)
                time.sleep(5)
        else:
            print(cs(f"\nSkipped as date is less than cut off date", "red"))

    def pdf_file_exists(self, pdf_name):
        self.pdf_name = pdf_name
        self.root = config.ROOT_DIR
        self.root = Path(self.root).expanduser()
        self.pdfs = Path(self.root).rglob("*.pdf")
        self.pdf_list = []

        for pdf in self.pdfs:
            self.pdf_list.append(pdf.name)
        if self.pdf_name in chain(self.pdf_list):
            return True
        else:
            return False

    def check_date(self, news_date):
        self.news_date = datetime.strptime(news_date, "%Y/%b/%d")
        self.cutoff_date = datetime.strptime(config.CUTOFF_DATE, "%d/%m/%Y")
        if self.news_date < self.cutoff_date:
            return False
        else:
            return True

    # def csvwriter(self, newspaper, name, link, downloaded=True):
    #     self.newspaper = newspaper
    #     self.name = name
    #     self.link = link
    #     self.downloaded = downloaded

    #     if downloaded:
    #         csv_file = "downloaded_papers.csv"
    #     else:
    #         csv_file = "failed_to_download.csv"

    #     with open(csv_file, "a") as csvfile:
    #         csvwriter = csv.writer(csvfile, delimiter=",")
    #         csvwriter.writerow(fields)
    #         csvwriter.writerow([self.newspaper, self.name, self.link])
