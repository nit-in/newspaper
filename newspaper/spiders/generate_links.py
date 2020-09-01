#!/usr/bin/python3
import newspaper.spiders.config as config
import random


def generate_links(newspaper, tag):
    link_list = []
    for num in range(1, int(config.UPPER_RANGE) + 1):
        if newspaper == "business_standard":
            urls = (
                config.BUSINESS_STANDARD
                + str(tag)
                + "&page="
                + str(num)
                + "&type=print-media"
            )
        if newspaper == "the_hindu":
            urls = (
                config.THE_HINDU
                + str(num)
                + "&moreContactsAvailable=true&query="
                + str(tag)
            )
        if newspaper == "livemint":
            urls = config.LIVEMINT + str(num) + "/" + str(tag)
        if newspaper == "economic_times":
            urls = config.ECONOMIC_TIMES + str(tag) + "&curpg=" + str(num)

        link_list.append(urls)
    random.shuffle(link_list, random.random)
    return link_list
