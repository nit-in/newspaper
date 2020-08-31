#!/usr/bin/python3
import os.path
import subprocess
from stringcolor import *
import functools
import csv
import newspaper.spiders.config as config
import pdfkit
from pathlib import Path

# fields = ["Newspaper", "File_Name", "Link"]


class make_pdf:
    """generate pdf from newspaper links,also csv files for successful and failed downloads"""

    def __init__(self, newspaper, link, article_date, tag, file_name):
        self.newspaper = newspaper
        self.link = link
        self.article_date = article_date
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
        print("Working...")
        options = config.PDFKIT_OPTIONS
        if self.pdf_path.parent.is_dir():
            print(f"Folder: {self.pdf_path.parent} already exixts")
        else:
            print(f"making {self.pdf_path.parent} folder")
            self.pdf_path.parent.mkdir(parents=True)
        # self.file_name = os.path.join(self.folder,self.file_name + ".pdf")
        if self.pdf_path.exists() and int(self.pdf_path.lstat().st_size) > 25600:
            print(f"File: {self.pdf_path} already downloaded")
        else:
            print(f"Downloading: {self.pdf_path}")
            pdfkit.from_url(str(self.link), str(self.pdf_path), options=options)

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
