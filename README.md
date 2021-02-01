# newspaper
python program with scrapy spider to search newspaper site and download webpage as pdf


## Usage:

To use the newspaper spider

**Clone the git or download:**

    git clone https://github.com/nit-in/news-paper.git
    
**enter the news-paper diretory:**
    
    cd news-paper

**Install required packages:**

    pip install -r requirements.txt

**Command to use:**

  `scrapy crawl business_standard`
  
  `scrapy crawl economic_times`
  
  `scrapy crawl livemint`

  `scrapy crawl the_hindu`

  `scrapy crawl indian_express`

  `scrapy crawl financial_express`
 
if you do not want any logs
run these as

  `scrapy crawl --nolog business_standard`
  
  `scrapy crawl --nolog economic_times`
  
  `scrapy crawl --nolog livemint`
  
  `scrapy crawl --nolog the_hindu`

  `scrapy crawl --nolog indian_express`

  `scrapy crawl --nolog financial_express`


This will create a folder in your home directory i.e. **~/newspaper**

Pdfs will be saved in this folder
You can change this from config.py file **ROOT_DIR**
