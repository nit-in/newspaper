#!/usr/bin/python3

ROOT_DIR = "~/newspaper/"
JSON_FILE = "newspaper/spiders/terms.json"
UPPER_RANGE = 2
BUSINESS_STANDARD_ROOT = "https://www.business-standard.com"
BUSINESS_STANDARD = (
    "https://www.business-standard.com/request-handler/article/ajax-search?keyword="
)
BUSINESS_STANDARD_PRINT = (
    "https://www.business-standard.com/article/printer-friendly-version?article_id="
)
ECONOMIC_TIMES = (
    "https://economictimes.indiatimes.com/topics_all.cms?type=article&query="
)
INDIAN_EXPRESS_ROOT = "https://indianexpress.com/"
ECONOMIC_TIMES_ROOT = "https://economictimes.indiatimes.com"
LIVEMINT_ROOT = "https://livemint.com/"
LIVEMINT = "https://www.livemint.com/searchlisting/"
LIVEMINT_PRINT = "https://www.livemint.com/fullStory/"
THE_HINDU_ROOT = "https://thehindu.com"
THE_HINDU = "https://zdwidget3-bs.sphereup.com/Search?url=https://www.thehindu.com/&isDescending=true&sortOn=date&accountId=69878363&sessionId=undefined&limit=5&page="
FINANCIAL_EXPRESS_ROOT = "https://www.financialexpress.com/"
FINANCIAL_EXPRESS = "https://www.financialexpress.com/page/"

PDFKIT_OPTIONS = {
    "page-size": "A4",
    "encoding": "UTF-8",
    "enable-javascript": "",
    "javascript-delay": "5000",
    "images": "",
    "background": "",
    "no-stop-slow-scripts": "",
}
